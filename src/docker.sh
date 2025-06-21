#!/bin/sh
echo "Current directory: $(pwd)"
files=$(ls)
echo "Files in current directory:"
for file in $files; do
  echo "$file"
done
if [ -f "__main__.py" ]; then
  python3 __main__.py -c ./config
else
  echo "__main__.py not found in $(pwd)"
  exit 1
fi


# if [ -d "NewsExtraction" ]; then
#   cd NewsExtraction
#   if [ -f "./__main__.py" ]; then
#     python3 ./__main__.py
#   else
#     echo "__main__.py not found in NewsExtraction directory."
#     exit 1
#   fi
# else
#   echo "Directory NewsExtraction does not exist."
#   exit 1
# fi