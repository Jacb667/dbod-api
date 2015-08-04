ARCH=x86_64
RPMBUILD=rpmbuild
RPMFLAGS=-ba
SRCPATH=${HOME}/rpmbuild
SPECPATH=$(SRCPATH)/SPECS
SOURCESPATH=$(SRCPATH)/SOURCES
RPMPATH=$(SRCPATH)/RPMS/$(ARCH)
SPECFILE=dbod-api.spec
VERSION=0.5.0

# The tar file needs to be in the repo as the Mock environment doesn't have
sources:
	tar cvzf dbod-api-${VERSION}.tar.gz bin/ dbod/ requirements.pip setup.py setup.cfg 

# This task will generate an RPM locally
manual-rpm:  
	cp dbod-api-*.tar.gz $(SOURCESPATH)
	$(RPMBUILD) $(RPMFLAGS) dbod-api.spec

clean:
	rm -f dbod-api-*.tar.gz
