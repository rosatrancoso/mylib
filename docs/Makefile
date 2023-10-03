# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS       ?=
SPHINXBUILD      ?= sphinx-build
IS_COMMIT_TAGGED ?= false
CONF_FILE         = conf.py
SOURCE_DIR        = _source
BUILD_DIR         = _build
PUBLISH_DST       = mylib

override ENV = dev
ifeq ($(IS_COMMIT_TAGGED),true)
	override ENV = prod
endif

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCE_DIR)" "$(BUILD_DIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCE_DIR)" "$(BUILD_DIR)" $(SPHINXOPTS) $(O)

clean_build:
	rm -rf $(BUILD_DIR)

clean_source:
	rm -rf $(SOURCE_DIR)

clean: clean_source clean_build

prep:
	rsync -rtpv source/ $(SOURCE_DIR)/
	cp -rpv $(CONF_FILE) $(SOURCE_DIR)/

api:
	sphinx-apidoc -e --ext-autodoc -f -o $(SOURCE_DIR)/api/package ../mylib
	sphinx-apidoc -e --ext-autodoc -f -o $(SOURCE_DIR)/api/scripts ../scripts

gen_html: clean_build
	@$(SPHINXBUILD) $(SOURCE_DIR) $(BUILD_DIR)

all: clean prep api gen_html ;
all2: clean prep gen_html ;

publish:
	aws s3 sync --delete --only-show-errors $(BUILD_DIR) s3://$$(aws ssm get-parameter --name /docs/$(ENV)/bucket_name --output text --query 'Parameter.Value')/$(PUBLISH_DST)
