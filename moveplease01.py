 #!/usr/bin/env python3
 # standard library imports
 import shutil  
 import os     

import shutil
import os
    #called at runtime
 os.chdir("/home/student/mycode/") 
 shutil.move("raynor.obj", "ceph_storage/")

     # program will pause while we accept input
     xname = input('What is the new name for kerrigan.obj? ') # collect string input from the user
     shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)  # moving kerrigan.obj into
                                                                        # ceph_storage/ with new name


 # this calls our main function

