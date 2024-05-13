.PHONY: recovery-bin deleted-blocks photo clean

clean:
	@rm -rf recover-deleted-blocks sur-restored.jpg

recovery-bin:
	@cp iTunes.app/CoreADI.pkg/Payload/System/Library/CoreServices/UAUPlugins/ADIUserAccountUpdater.bundle/Contents/MacOS/RecoverBlock recover-deleted-blocks

deleted-blocks: recover-deleted-blocks
	@./recover-deleted-blocks ios_data DCIM\x7HhA1wdfA > x7HhA1wdfA.bloc

photo: x7HhA1wdfA.bloc
	@python3 parse.py