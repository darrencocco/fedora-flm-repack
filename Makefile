MAKEFILE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

all: flm

all-srpm: srpm-flm

flm: srpm-flm build-flm

xrt-plugin-amdxdna: srpm-xrt-plugin-amdxdna build-xrt-plugin-amdxdna

amdxdna-kmod: srpm-amdxdna-kmod build-amdxdna-kmod

srpm-flm:
	$(MAKE) -f $(MAKEFILE_DIR)/.copr/Makefile clean
	$(MAKE) -f $(MAKEFILE_DIR)/.copr/Makefile srpm

build-flm:
	dnf builddep -y flm*.src.rpm
	rpmbuild -rb flm*.src.rpm
	cp ~/rpmbuild/RPMS/*/* ./

clean:
	$(MAKE) -f $(MAKEFILE_DIR)/.copr/Makefile clean
	rm -f *.rpm