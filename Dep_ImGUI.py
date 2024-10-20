#gets ImGUI

import GitOperations

#lists all the files we need to include
IMGUI_SOURCE_FILE_NAMES = [
	"imconfig.h",
	"imgui.h",
	"imgui.cpp",
	"imgui_draw.cpp",
	"imgui_internal.h",
	"imgui_tables.cpp",
	"imgui_widgets.cpp",
	"imstb_rectpack.h",
	"imstb_textedit.h",
	"imstb_truetype.h",
	"imgui_demo.cpp",
    
    "backends/imgui_impl_sdl2.cpp",
    "backends/imgui_impl_vulkan.cpp"
]

#adds the source paths to the source list in a Premake project
def AddSources_ImGUI(srcs):
	for f in IMGUI_SOURCE_FILE_NAMES:
		srcs.append(IMGUI_INCLUDE_DIR + "/" + f)

#clones ImGUI
def GetDep_ImGUI(vendersDir):
    GitOperations.GitClone("https://github.com/ocornut/imgui.git", VendersDir + "/ImGUI")

#gets the include directory
def GetIncludeDirectory(vendersDir):
    return vendersDir + "/ImGUI"