import qbs
import qbs.File
import qbs.TextFile
import qbs.FileInfo
import "installExtra/mainGroup.qbs" as MainGroup

Project {
  id: main
  property string name: "base"
  property string releaseType

  Probe {
    id: info
    property string fileName: "info.json"
    property var data
    configure: {
      // making sure the info file exists
      if (!File.exists(fileName)){
        throw new Error("Cannot find: " + fileName)
      }

      // parsing info contents
      data = JSON.parse(new TextFile(fileName).readAll())
      return data
    }
  }

  Application {
    name: "defaultPython"
    MainGroup {
      name: main.name
      version: info.data.version
      releaseType: main.releaseType
    }
  }
}
