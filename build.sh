#!/bin/sh


top_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $top_dir

echo TARGETS is $TARGETS

usage()
{
	echo "usage : $0 [options] target1 target2 ..."
	exit 0
}

all()
{
	config
	build
}

config()
{
	pushd $top_dir
	cmake -G "Unix Makefiles" .
	popd
}

build()
{
	pushd $top_dir
	cmake --build . -- all
	popd
}

kernel()
{
	pushd $top_dir
	rm -f CMakeCache.txt
	config
	cmake --build . -- clean kernel
	popd
}

driver()
{
	pushd $top_dir
	rm -f CMakeCache.txt
	config
	cmake --build . -- clean driver
	popd
}

cellos()
{
	pushd $top_dir
	rm -f CMakeCache.txt
	config
	cmake --build . -- clean cellos
	popd
}

bootrom()
{
	pushd $top_dir
	rm -f CMakeCache.txt
	config
	cmake --build . -- clean bootrom
	popd
}

startup()
{
	pushd $top_dir
	rm -f CMakeCache.txt
	config
	cmake --build . -- clean startup
	popd
}

qemu()
{
	cmake --build . -- qemu
}

clean()
{
	cmake --build . -- clean
}

mclean()
{
	rm -rf CMakeFiles
	rm -f CMakeCache.txt
}



logfile=""

while getopts hvl: option
do
	case "$option" in
		h)
			usage;;
		v)
			verbose=1;;
		l)
			logfile=$OPTARG;;
		*)
			echo unknown option "$option";;
	esac
done

shift $(($OPTIND-1))

if [ "x$logfile" != "x" ]; then
	echo logfile is $logfile
fi

for target in "$@ $TARGETS" ; do
	type -t $target
	res=`type -t $target | grep function`
	if [ "$res" = "function" ]; then
		$target
	else
		make $target
	fi
done

