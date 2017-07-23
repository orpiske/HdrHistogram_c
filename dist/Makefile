VERSION=0.9.6

check:
	rpmlint -i dist/hdr-histogram-c.spec

rpm-prep:
	mkdir -p ${HOME}/rpmbuild/SOURCES/
	tar --transform="s/\./hdr-histogram-c-${VERSION}/" -cf ${HOME}/rpmbuild/SOURCES/hdr-histogram-c-${VERSION}.tar.gz --exclude=./build --exclude=.git --exclude=*.bz ./ --gzip

rpm: rpm-prep
	rpmbuild -ba dist/hdr-histogram-c.spec
