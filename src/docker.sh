#!/bin/sh

#cd newsplease
#python __main__.py -c ./config
# cd /news-snippet/src/newsplease
# python3 -m pip install --upgrade pipconfig
# python3 __main__.py -c ./config

# Upgrade pipconfig (if needed)
python3 -m pip install --upgrade pipconfig

# Move to the NewExtration directory
cd ./NewExtration

# Run the package using the __main__.py entry point
python3 -m NewExtration