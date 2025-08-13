from cc3d.core.PySteppables import *
import numpy as np

class MesEpiFoldSteppable(SteppableBasePy):

    def __init__(self, frequency=1):

        SteppableBasePy.__init__(self,frequency)

    def start(self):
        """
        Called before MCS=0 while building the initial simulation
        """
        # Make sure ExternalPotential plugin is loaded
        cell = self.cell_field[175, 230, 0]
        cell2 = self.cell_field[125, 230, 0]
        self.shared_steppable_vars['moving_muscle_cell_lambdaVecY'] = 3.0 #define a global variable for force component pointing along Y axi
        # fetch the variable
        cell.lambdaVecY = self.shared_steppable_vars['moving_muscle_cell_lambdaVecY'] 
        cell2.lambdaVecY = self.shared_steppable_vars['moving_muscle_cell_lambdaVecY']   
        #setting the global variable
        self.shared_steppable_vars['moving_muscle_cell'] = cell
        self.shared_steppable_vars['moving_muscle_cell2'] = cell2
        #adding external force towards the middle for cells EPI and ECM
        # iterating over cells of type 1
        # list of  cell types (capitalized)
        
        #specifying the initial size for wall increments
        self.size=1    
        self.wallcell = self.new_cell(self.WALL)
        #create fpp links for epithelial cells
        # iterating over cells of type 1
        # list of  cell types (capitalized)
        # for cell in self.cell_list_by_type(self.EPI):
            # # you can access/manipulate cell properties here
            # # print ("id=", cell.id, " type=", cell.type)
            # for neighbor, common_surface_area in self.get_cell_neighbor_data_list(cell):
                # if neighbor:
                    # if neighbor.type==self.EPI:
                         # link = self.new_fpp_link(cell, neighbor, 10, 7, 1000)

            
        
        # Make sure FocalPointPlacticity plugin is loaded
        # Arguments are:
        # initiator: CellG, initiated: CellG, lambda_distance: float, target_distance: float, max_distance: float
       
        
        
        
        
    def step(self, mcs):

        if mcs % 6000==0 and mcs>=10:
            x = 0
            y = 278
            size = 7
            cell = self.new_cell(self.EPI)
            # size of cell will be SIZExSIZEx1
            self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell

            # for neighbor, common_surface_area in self.get_cell_neighbor_data_list(cell):
                # if neighbor:
                    # if neighbor.type==self.EPI:
                         # link = self.new_fpp_link(cell, neighbor, 10, 7, 1000)
            
            x = 0
            y = 271
            size = 7
            cell = self.new_cell(self.ECM)
            # size of cell will be SIZExSIZEx1
            self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
            
        if mcs % 6000==0 and mcs>=10:
            x = 0
            y = 200
            size = 7
            cell = self.new_cell(self.MUSCLE)
            # size of cell will be SIZExSIZEx1
            self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell

            # for neighbor, common_surface_area in self.get_cell_neighbor_data_list(cell):
                # if neighbor:
                    # if neighbor.type==self.EPI:
                         # link = self.new_fpp_link(cell, neighbor, 10, 7, 1000)    
        
        if mcs % 6000==0:
                x = 0
                y = 250
                size = 7
                cell = self.new_cell(self.STROMA)
                # size of cell will be SIZExSIZEx1
                self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
                
                x = 0
                y = 257
                size = 7
                cell = self.new_cell(self.STROMA)
                # size of cell will be SIZExSIZEx1
                self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
                
                x = 0
                y = 264
                size = 7
                cell = self.new_cell(self.STROMA)
                # size of cell will be SIZExSIZEx1
                self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
                
        if mcs%100==0:
            for cell in self.cell_list_by_type(self.EPI, self.ECM):    #This statement is doing the same thing as the line 119 -- 128
                # you can access/manipulate cell properties here
                # if cell.xCOM<self.dim.x:
                    # direction = -1
                # else:
                    # direction = +1
                direction = (cell.xCOM-self.dim.x)/(self.dim.x/2)    
                cell.lambdaVecX = direction*0.5  # force component pointing along X axis - towards positive X's
                
        if mcs%100==0 and mcs<4000:
            for cell in self.cell_list_by_type(self.EPI, self.ECM):
                # you can access/manipulate cell properties here
                # if cell.xCOM<self.dim.x:
                    # direction = -1
                # else:
                    # direction = +1
                direction = (cell.xCOM-self.dim.x)/(self.dim.x/2)
                cell.lambdaVecX = direction*0.5  # force component pointing along X axis - towards positive X's
                # Make sure ExternalPotential plugin is loaded
               
                
                
        if mcs>=4000 and mcs%100==0:
            for cell in self.cell_list_by_type(self.EPI, self.ECM):
                # you can access/manipulate cell properties here
                # if cell.xCOM<self.dim.x:
                    # direction = -1
                # else:
                    # direction = +1
                direction = (cell.xCOM-self.dim.x)/(self.dim.x/2)
                
                #assign force direction based on location of cell
         
                cell.lambdaVecX = direction*1.0  # force component pointing along X axis - towards positive X's  
              
                
        if mcs>=4000 and mcs%100==0:
            for cell in self.cell_list_by_type(self.STROMA):
                # you can access/manipulate cell properties here
                # if cell.xCOM<self.dim.x:
                    # direction = -1
                # else:
                    # direction = +1
                direction = (cell.xCOM-self.dim.x)/(self.dim.x/2)    
                cell.lambdaVecX = direction*0.5  # force component pointing along X axis - towards positive X's       
            
                if 120<cell.xCOM<220:
                    cell.lambdaVecY = 1.5 #force in the Y direction for central stromal cells
        
        if mcs>=4000 and mcs%100==0:
            for cell in self.cell_list_by_type(self.MUSCLE):
                # you can access/manipulate cell properties here
                # if cell.xCOM<self.dim.x:
                    # direction = -1
                # else:
                    # direction = +1
                  
            
                if 120<cell.xCOM<210:
                    cell.lambdaVecY = 6.0 #force in the Y direction for central muscle cells
                    

        
                    
        
        
        # # Make sure ExternalPotential plugin is loaded
        # if mcs%10==0 and self.size<50:
            # Xdim = self.dim.x
            # Ydim = self.dim.y

            # # size of cell will be SIZExSIZEx1
            # self.cell_field[self.size-1:self.size, 0:Ydim, 0] = self.wallcell
            # self.cell_field[Xdim-self.size:Xdim-self.size+1, 0:Ydim, 0] = self.wallcell
            # self.size=self.size+1
        
        
        # if mcs>=5000 and mcs%100==0:
            # #fetching the moving muscle cell
            # cell = self.shared_steppable_vars['moving_muscle_cell']
            # # Make sure ExternalPotential plugin is loaded
            # if cell.yCOM<=75:
                # cell.lambdaVecY = self.shared_steppable_vars['moving_muscle_cell_lambdaVecY']/5  # force component pointing along Y axis - towards negative Y's
            # else:
                # cell.lambdaVecY = self.shared_steppable_vars['moving_muscle_cell_lambdaVecY']  # force component pointing along Y axis - towards negative Y's
            
            # cell = self.shared_steppable_vars['moving_muscle_cell2']
            # # Make sure ExternalPotential plugin is loaded
            # if cell.yCOM<=75:
                # cell.lambdaVecY = self.shared_steppable_vars['moving_muscle_cell_lambdaVecY']/5  # force component pointing along Y axis - towards negative Y's
            # else:
                # cell.lambdaVecY = self.shared_steppable_vars['moving_muscle_cell_lambdaVecY']  # force component pointing along Y axis - towards negative Y's
            
            
            

    def finish(self):
        """
        Called after the last MCS to wrap up the simulation
        """

    def on_stop(self):
        """
        Called if the simulation is stopped before the last MCS
        
        
        """
        
        
class MitosisSteppable(MitosisSteppableBase):
    def __init__(self, frequency=1):
        MitosisSteppableBase.__init__(self, frequency)
        
        # self.STROMA = 2
        
        
    def step(self, mcs):
        
        # if mcs == 6000:
            # for cell in self.cell_list_by_type(self.STROMA): 
                # if 200 < cell.xCOM < 300:
                    # self.divide_cell_random_orientation(cell)
                    
        # if mcs == 6000:
            # for cell in self.cell_list_by_type(self.STROMA): 
                # if 240 < cell.xCOM < 280:
                    # self.divide_cell_random_orientation(cell)             
                    
                    
                    
        if mcs == 8000: 
            for cell in self.cell_list_by_type(self.MUSCLE):
                if 50 <cell.xCOM< 300:
                    self.divide_cell_random_orientation(cell)
                    
            # for cell in self.cell_list_by_type(self.MUSCLE):
                # if 60 <cell.xCOM< 130:
                    # self.divide_cell_random_orientation(cell)        
                    
        if mcs == 6000:
            for cell in self.cell_list_by_type(self.STROMA): 
                if 200 < cell.xCOM < 300:
                    self.divide_cell_random_orientation(cell)  # microns/pixels            
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        