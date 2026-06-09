spec := flm.spec
outdir := ./
VERSION := $(shell rpmspec --query --queryformat=%{VERSION} $(spec))
GIT_DIR := flm-$(VERSION)
ARCHIVE := $(GIT_DIR).tar.gz
SPEC_FILENAME := $(notdir $(spec))

srpm: prepare
	rpmbuild --define "_topdir `pwd`/rpmbuild" --undefine dist -bs rpmbuild/SPECS/$(SPEC_FILENAME)
	cp rpmbuild/SRPMS/* $(outdir)

prepare: download
	mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
	cp $(ARCHIVE) rpmbuild/SOURCES/
	cp $(spec) rpmbuild/SPECS/

download:
	dnf install -y git
	git clone --recursive --branch v$(VERSION) https://github.com/FastFlowLM/FastFlowLM.git $(GIT_DIR)
	tar -czf $(ARCHIVE) $(GIT_DIR)

clean:
	rm -f $(ARCHIVE)
	rm -rf $(GIT_DIR)/
	rm -rf rpmbuild/