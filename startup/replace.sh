#!/bin/sh

obj_path=`find ./CMakeFiles/ -name "*.obj"`

echo $obj_path

cat cellos.lds.in | \
	sed -e "s|@CELLSTARTUP_OBJ@|$obj_path|" > \
	cellos.lds


