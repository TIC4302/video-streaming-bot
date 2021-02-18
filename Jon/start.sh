#!/bin/bash

xauth list | head -n 1 | sed 's/unix:/unix:0/g' > init-script.bash &&  sed -i 's/^/xauth add /' init-script.bash && sed -i 's|^|#/bin/bash\n|' init-script.bash

chmod +x init-script.bash
