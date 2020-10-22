#!/bin/sh


top_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $top_dir
source ./powerpc-eabi-gcc.bashrc

RSYNC="rsync -rlOtcv"

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
	cmake .
	popd
}

build()
{
	pushd $top_dir
	make
	popd
}

kernel()
{
	pushd $top_dir
	rm -f CMakeCache.txt
	config
	make kernel
	$RSYNC $top_dir/kernel/ /home/share/cellos_cmake_bin/kernel/
	popd
}

driver()
{
	pushd $top_dir
	rm -f CMakeCache.txt
	config
	make driver
	$RSYNC -av $top_dir/driver/ /home/share/cellos_cmake_bin/driver
	popd
}

cellos()
{
	pushd $top_dir
	rm -f CMakeCache.txt
	config
	make cellos
	$RSYNC -av $top_dir/cellos/ /home/share/cellos_cmake_bin/cellos
	popd
}

bootrom()
{
	pushd $top_dir
	rm -f CMakeCache.txt
	config
	make bootrom
	$RSYNC -av $top_dir/bootrom/ /home/share/cellos_cmake_bin/bootrom
	popd
}

startup()
{
	pushd $top_dir
	rm -f CMakeCache.txt
	config
	make startup
	$RSYNC -av $top_dir/startup/ /home/share/cellos_cmake_bin/startup
	popd
}

clean()
{
	make clean
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

for target in "$@" ; do
	type -t $target
	res=`type -t $target | grep function`
	if [ "$res" = "function" ]; then
		echo $target is function
		$target
	else
		make $target
	fi
done

