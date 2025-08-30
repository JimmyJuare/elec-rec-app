const { contextBridge } = require('electron')

contextBridge.exposeInMainWorld('electronAPI', {
  // you can add safe functions here for React to call
})
