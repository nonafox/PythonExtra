CROSS_COMPILE := sh-elf-

include $(TOP)/py/py.mk
include $(TOP)/extmod/extmod.mk

CFLAGS += -m4-nofpu -mb -fstrict-volatile-bitfields \
          -I. -I$(TOP)/ports/sh -I$(BUILD) -I$(TOP) \
          $(SH_CFLAGS) -Os -Wall -Wextra -Wno-unused-parameter
LIBS += -nostdlib -Wl,--no-warn-rwx-segments $(SH_LDFLAGS) -Wl,-Map=build/map

# Source files
SRC_C = \
    ports/sh/main.c \
    ports/sh/console.c \
    ports/sh/debug.c \
    ports/sh/keymap.c \
    ports/sh/modcasioplot.c \
    ports/sh/modgint.c \
    ports/sh/mphalport.c \
    ports/sh/objgintimage.c \
    ports/sh/pyexec.c \
    ports/sh/stredit.c \
    ports/sh/widget_shell.c \
    shared/runtime/gchelper_generic.c \
    shared/runtime/stdout_helpers.c \
    shared/runtime/interrupt_char.c \

SRC_QSTR += \
    ports/sh/main.c \
    ports/sh/modcasioplot.c \
    ports/sh/modgint.c \
    ports/sh/objgintimage.c \
    ports/sh/pyexec.c \


ifeq ($(TARGETCASIO),"FXCG50")
    $(info ************  FXCG50 VERSION ************ )

    $(info *********  Add IO FileIO module ********* )  
    SRC_C += \
        ports/sh/fileio/file.c

    SRC_QSTR += \
        ports/sh/fileio/file.c


    $(info *********  Add Numworks modules ********* )  
    SRC_C += \
        ports/sh/numworks/modkandinsky.c \
        ports/sh/numworks/ion.c \
        ports/sh/numworks/time.c

    SRC_QSTR += \
        ports/sh/numworks/modkandinsky.c \
        ports/sh/numworks/ion.c \
        ports/sh/numworks/time.c


    $(info ***********  Add µlab modules *********** )  
    CFLAGS_EXTRA += -DMODULE_ULAB_ENABLED=1    
    
    SRC_C += \
        ports/sh/ulab/scipy/linalg/linalg.c \
        ports/sh/ulab/scipy/optimize/optimize.c \
        ports/sh/ulab/scipy/signal/signal.c \
        ports/sh/ulab/scipy/special/special.c \
        ports/sh/ulab/ndarray_operators.c \
        ports/sh/ulab/ulab_tools.c \
        ports/sh/ulab/ndarray.c \
        ports/sh/ulab/numpy/ndarray/ndarray_iter.c \
        ports/sh/ulab/ndarray_properties.c \
        ports/sh/ulab/numpy/approx.c \
        ports/sh/ulab/numpy/bitwise.c \
        ports/sh/ulab/numpy/compare.c \
        ports/sh/ulab/numpy/carray/carray.c \
        ports/sh/ulab/numpy/carray/carray_tools.c \
        ports/sh/ulab/numpy/create.c \
        ports/sh/ulab/numpy/fft/fft.c \
        ports/sh/ulab/numpy/fft/fft_tools.c \
        ports/sh/ulab/numpy/filter.c \
        ports/sh/ulab/numpy/io/io.c \
        ports/sh/ulab/numpy/linalg/linalg.c \
        ports/sh/ulab/numpy/linalg/linalg_tools.c \
        ports/sh/ulab/numpy/numerical.c \
        ports/sh/ulab/numpy/poly.c \
        ports/sh/ulab/numpy/random/random.c \
        ports/sh/ulab/numpy/stats.c \
        ports/sh/ulab/numpy/transform.c \
        ports/sh/ulab/numpy/vector.c \
        ports/sh/ulab/numpy/numpy.c \
        ports/sh/ulab/scipy/scipy.c \
        ports/sh/ulab/user/user.c \
        ports/sh/ulab/utils/utils.c \
        ports/sh/ulab/ulab.c

    SRC_QSTR += \
        ports/sh/ulab/scipy/linalg/linalg.c \
        ports/sh/ulab/scipy/optimize/optimize.c \
        ports/sh/ulab/scipy/signal/signal.c \
        ports/sh/ulab/scipy/special/special.c \
        ports/sh/ulab/ndarray_operators.c \
        ports/sh/ulab/ulab_tools.c \
        ports/sh/ulab/ndarray.c \
        ports/sh/ulab/numpy/ndarray/ndarray_iter.c \
        ports/sh/ulab/ndarray_properties.c \
        ports/sh/ulab/numpy/approx.c \
        ports/sh/ulab/numpy/bitwise.c \
        ports/sh/ulab/numpy/compare.c \
        ports/sh/ulab/numpy/carray/carray.c \
        ports/sh/ulab/numpy/carray/carray_tools.c \
        ports/sh/ulab/numpy/create.c \
        ports/sh/ulab/numpy/fft/fft.c \
        ports/sh/ulab/numpy/fft/fft_tools.c \
        ports/sh/ulab/numpy/filter.c \
        ports/sh/ulab/numpy/io/io.c \
        ports/sh/ulab/numpy/linalg/linalg.c \
        ports/sh/ulab/numpy/linalg/linalg_tools.c \
        ports/sh/ulab/numpy/numerical.c \
        ports/sh/ulab/numpy/poly.c \
        ports/sh/ulab/numpy/random/random.c \
        ports/sh/ulab/numpy/stats.c \
        ports/sh/ulab/numpy/transform.c \
        ports/sh/ulab/numpy/vector.c \
        ports/sh/ulab/numpy/numpy.c \
        ports/sh/ulab/scipy/scipy.c \
        ports/sh/ulab/user/user.c \
        ports/sh/ulab/utils/utils.c \
        ports/sh/ulab/ulab.c
    
endif

ifeq ($(TARGETCASIO),"FX9860G")
    $(info ***********  FX9860G  VERSION *********** )

    $(info *********  Add IO FileIO module ********* )  
    SRC_C += \
        ports/sh/fileio/file.c

    SRC_QSTR += \
        ports/sh/fileio/file.c

endif


ASSETS_O := $(SH_ASSETS:%=$(BUILD)/sh_assets/%.o)

OBJ = $(PY_O) $(ASSETS_O) $(addprefix $(BUILD)/, $(SRC_C:.c=.o))

$(BUILD)/firmware.bin: $(BUILD)/firmware.elf
	$(Q)$(CC:gcc=objcopy) -O binary -R .bss -R .gint_bss $< $@

$(BUILD)/firmware.elf: $(OBJ)
	$(ECHO) "LINK $@"
	$(Q)$(CC) $(LDFLAGS) -o $@ $^ $(LIBS)
	$(Q)$(SIZE) $@

$(BUILD)/sh_assets/%.o: % $(SH_METADATA)
	$(Q)mkdir -p $(dir $@)
	$(Q)fxconv --toolchain=$(CROSS_COMPILE:%-=%) $(SH_CONVFLAGS) $< -o $@

ARCHIVE := PythonExtra-$(shell git describe).zip

# Weird rules calling back to fxcg50 and fx9860g3, both of whic include this
release:
	$(MAKE) -C ../fx9860g3
	$(MAKE) -C ../fxcg50
	cd ../sh && zip "$(ARCHIVE)" -j ../fx9860g3/PythonEx.g1a ../fxcg50/PythonExtra.g3a
	cd ../sh && zip "$(ARCHIVE)" -r examples modules

.PHONY: release
.PRECIOUS: $(ARCHIVE)

include $(TOP)/py/mkrules.mk
