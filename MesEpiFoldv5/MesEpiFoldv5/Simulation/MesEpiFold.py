
from cc3d import CompuCellSetup
        

from MesEpiFoldSteppables import MesEpiFoldSteppable
CompuCellSetup.register_steppable(steppable=MesEpiFoldSteppable(frequency=1))


from MesEpiFoldSteppables import MitosisSteppable
CompuCellSetup.register_steppable(steppable=MitosisSteppable(frequency=1))


CompuCellSetup.run()

