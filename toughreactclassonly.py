# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:42:01 2019

@author: tajayi3
"""

class toughreact_tecplot(object):
    """Class for TOUGHREACT Tecplot output files. These work similarly to
    t2listing objects, but have just a single element table at each
    time. It is possible to navigate through time by using the next()
    and prev() functions to step through, or using the first() and
    last() functions to go to the start or end, or to set the index,
    step (model time step number) or time properties directly.  When
    reading a toughreact_tecplot object from file it is necessary also
    to specify the block names (as these are not stored in the Tecplot
    file).
    """
    def __init__(self, filename, blocks):
        self.filename = filename
        self._file = open(filename, 'rU')
        self.setup_pos()
        self.setup_table(blocks)
        if self.num_times > 0:
            self._index = 0
            self.first()
        else: raise Exception('No results found in TOUGHREACT Tecplot file ' + filename)

    def __repr__(self): return "TOUGHREACT results for " + str(self.element.num_rows) + " blocks"

    def get_index(self): return self._index
    def set_index(self, i):
        self._file.seek(self._pos[i])
        self._index = i
        if self._index < 0: self._index += self.num_times
        self.read_table()
    index = property(get_index, set_index)

    def get_time(self): return self.times[self._index]
    def set_time(self, t):
        if t < self.times[0]: self.index=0
        elif t > self.times[-1]: self.index = -1
        else:
            dt = np.abs(self.times - t)
            self.index = np.argmin(dt)
    time = property(get_time, set_time)

    def get_num_times(self): return len(self.times)
    num_times = property(get_num_times)

    def rewind(self):
        """Rewinds to start (without reading any results)"""
        self._file.seek(0)
        self._index = -1

    def first(self): self.index = 0
    def last(self): self.index = -1
    def next(self):
        """Find and read next set of results; returns false if at end of file"""
        more = self.index < self.num_times - 1
        if more: self.index += 1
        return more
    def prev(self):
        """Find and read previous set of results; returns false if at start of file"""
        more = self.index > 0
        if more: self.index -= 1
        return more

    def skipto(self, keyword, count = False):
        """Advances file to next line starting with specified keyword, returning the line."""
        if isinstance(keyword, list): keywords = keyword
        else: keywords = [keyword]
        line = ''
        num_lines = 0
        while not any([line.startswith(kw) for kw in keywords]):
            line = self._file.readline()
            num_lines += 1
            if line == '': return None, num_lines
        if count: return line, num_lines
        else: return line

    def find_next_time(self):
        """Advances to set of results at next time, and returns the time value."""
        line, num_lines = self.skipto(['ZONE', 'Zone', 'zone'], count = True)
        if line is None: return None, num_lines
        quotepos = line.find('"')
        if quotepos >= 0:
            spacepos = line.find(' ', quotepos)
            if spacepos >= 0: return float(line[quotepos+1:spacepos]), num_lines
            else: return None, num_lines
        else: return None, num_lines

    def setup_pos(self):
        """Sets up _pos list for TOUGHREACT Tecplot files, containing file position at the start
        of each set of results. Also sets up the times array."""
        self._file.seek(0)
        self._pos = []
        t = []
        endfile = False
        num_blocks = None
        while not endfile:
            time, num_lines = self.find_next_time()
            if time is not None:
                self._pos.append(self._file.tell())
                t.append(time)
            else: endfile = True
            if num_lines: num_blocks = num_lines - 1
        self.times = np.array(t)
        self._num_blocks = num_blocks

    def setup_table(self, blocks):
        """Sets up element table structure. Table columns are read from the VARIABLES line in the file.
        Table rows are block names, supplied as a list of strings, or taken from a mulgrid or t2data
        object."""
        import mulgrids as mg
        import t2grids as t2g
        if isinstance(blocks, mg.mulgrid): blocks = blocks.block_name_list
        elif isinstance(blocks, t2g.t2grid): blocks = [blk.name for blk in  blocks.blocklist]
        if len(blocks) != self._num_blocks:
            raise Exception("Specified block name list is the wrong length for " +
                            "TOUGHREACT Tecplot file "+ self.filename)
        self._file.seek(0)
        line = self.skipto(['VARIABLES', 'Variables', 'variables'])
        if line is not None:
            eqpos = line.find('=')
            sep = ',' if ',' in line else None
            rawcols = line[eqpos+1:].strip().split(sep)
            cols = []
            for col in rawcols:
                colstrip = col.strip()
                if colstrip:
                    if col.startswith('"') and col.endswith('"'):
                        cols.append(col[1:-1].strip())
                    else:
                        cols.append(colstrip)
            self.element = listingtable(cols, blocks, num_keys = 1)
        else:
            raise Exception("Could not find variable definitions " +
                            "for TOUGHREACT Tecplot file " + self.filename)

    def read_table_line(self, line):
        """Parses given string and returns an array of float values."""
        return np.fromstring(line, sep = ' ')

    def read_table(self):
        """Reads table data at the current time."""
        for i,blk in enumerate(self.element.row_name):
            line = self._file.readline().strip()
            self.element[i] = self.read_table_line(line)

    def history(self, selection):
        """Returns time histories for specified selection of block names (or
        index) and column names."""

        def ordered_selection(selection):
            osel = []
            for sel_index,(key,h) in enumerate(selection):  # convert keys to indices as necessary
                if isinstance(key, int): index = key
                else:
                    if key in self.element.row_name: index = self.element._row[key]
                    else: index = None
                if index is not None: osel.append((index,h,sel_index))
            osel.sort()
            return osel

        old_index = self.index
        if isinstance(selection, tuple): selection = [selection]
        osel = ordered_selection(selection)
        if len(osel) == 0: return None # no valid specifications
        hist = [[] for s in selection]
        self.rewind()

        for ipos,pos in enumerate(self._pos):
            self._file.seek(pos)
            self._index = ipos
            index = 0
            line = self._file.readline()
            for (lineindex, colname, sel_index) in osel:
                if lineindex is not None:
                    for k in range(lineindex-index): line = self._file.readline()
                    index = lineindex
                    vals = self.read_table_line(line)
                    valindex = self.element._col[colname]
                    hist[sel_index].append(vals[valindex])
        self._index = old_index
        result = [(self.times,np.array(h)) for sel_index,h in enumerate(hist)]
        if len(result) == 1: result = result[0]
        return result

    def get_vtk_data(self, geo, grid = None, geo_matches = True, blockmap = {}):
        """Returns dictionary of VTK data arrays from Tecplot file at current time."""
        from vtk import vtkFloatArray
        natm = geo.num_atmosphere_blocks
        nele = geo.num_underground_blocks
        arrays = {'Block':{}, 'Node':{}}
        for name in self.element.column_name: arrays['Block'][name] = vtkFloatArray()
        array_length = {'Block':nele, 'Node':0}
        array_data = {'Block':{}, 'Node':{}}
        def mname(blk): return blockmap[blk] if blk in blockmap else blk
        for array_type,array_dict in arrays.items():
            for name,array in array_dict.items():
                array.SetName(name)
                array.SetNumberOfComponents(1)
                array.SetNumberOfValues(array_length[array_type])
                if geo_matches: array_data[array_type][name] = self.element[name][natm:] # faster
                else:  # more flexible
                    array_data[array_type][name] = np.array([self.element[mname(blk)][name]
                                                             for blk in geo.block_name_list[natm:]])

        for array_type,data_dict in array_data.items():
            for name,data in data_dict.items():
                for iblk in range(nele):
                    arrays[array_type][name].SetValue(iblk, data[iblk])
        return arrays

    def write_vtk(self, geo, filename, grid = None, indices = None, start_time = 0.0,
                  time_unit = 's', blockmap = {}, surface_snap = 0.1):
        """Writes VTK files for a vtkUnstructuredGrid object corresponding to
        the grid in 3D with the Tecplot data, with the specified
        filename, for visualisation with VTK.  A t2grid can optionally
        be specified, to include rock type data as well.  A list of
        the required time indices can optionally be specified.
        """
        from vtk import vtkXMLUnstructuredGridWriter
        from os.path import splitext
        base, ext = splitext(filename)
        geo_matches = geo.block_name_list == self.element.row_name
        arrays = geo.get_vtk_data(blockmap)
        if grid is not None:
            grid_arrays = grid.get_vtk_data(geo, blockmap)
            for array_type,array_dict in arrays.items():
                array_dict.update(grid_arrays[array_type])
        import xml.dom.minidom
        pvd = xml.dom.minidom.Document()
        vtkfile = pvd.createElement('VTKFile')
        vtkfile.setAttribute('type','Collection')
        pvd.appendChild(vtkfile)
        collection = pvd.createElement('Collection')
        initial_index = self.index
        if indices is None: indices = range(self.num_times)
        yr = 3600. * 24 * 365.25
        timescales = {'s': 1.0, 'h': 3600., 'd': 3600. * 24, 'y': yr}
        if time_unit in timescales:
            timescale = timescales[time_unit] / yr # assumes Tecplot times are in years
        else: timescale = 1.0
        writer = vtkXMLUnstructuredGridWriter()
        for i in indices:
            self.index = i
            t = start_time + self.time / timescale
            filename_time = base + '_' + str(i) + '.vtu'
            results_arrays = self.get_vtk_data(geo, grid, geo_matches = geo_matches,
                                               blockmap = blockmap)
            for array_type,array_dict in arrays.items():
                array_dict.update(results_arrays[array_type])
            vtu = geo.get_vtk_grid(arrays, surface_snap)
            writer.SetFileName(filename_time)
            if hasattr(writer, 'SetInput'): writer.SetInput(vtu)
            elif hasattr(writer, 'SetInputData'): writer.SetInputData(vtu)
            writer.Write()
            dataset = pvd.createElement('DataSet')
            dataset.setAttribute('timestep', str(t))
            dataset.setAttribute('file', filename_time)
            collection.appendChild(dataset)
        vtkfile.appendChild(collection)
        pvdfile = open(base+'.pvd', 'w')
        pvdfile.write(pvd.toprettyxml())
        pvdfile.close()
        self.index = initial_index