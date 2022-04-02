
	    grid[0][i].make_barrier()
	    grid[i][0].make_barrier()
	
	for i in range(len(grid[-1])):
	    grid[-1][i].make_barrier()
	    grid[i][-1].make_barrier()