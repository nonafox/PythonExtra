include ../../py/mkenv.mk

SH_CFLAGS := -DFX9860G
TARGETCASIO := "FX9860G"
SH_LDFLAGS := -T fx9860g.ld -ljustui-fx -lm -lgint-fx -lc -lgint-fx -lgcc

SH_ASSETS := \
  img_fkeys_main.png img_modifier_states.png \
  font_5x7.png font_4x4.png font_4x6.png font_3x5.png
SH_METADATA := fxconv-metadata.txt
SH_CONVFLAGS := --fx

all: PythonEx.g1a

beta: PyExBeta.g1a

PythonEx.g1a: $(BUILD)/firmware.bin icon.png
	fxgxa --g1a -n PythonExtra -i icon.png $< -o $@

PyExBeta.g1a: $(BUILD)/firmware.bin iconBeta.png
	fxgxa --g1a -n PyExBeta -i iconBeta.png $< -o $@

send: all
	fxlink -sw PythonEx.g1a

include $(TOP)/ports/sh/Makefile
