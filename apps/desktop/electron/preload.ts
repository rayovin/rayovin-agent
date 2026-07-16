import { contextBridge, ipcRenderer, webUtils } from 'electron'

contextBridge.exposeInMainWorld('rayovinDesktop', {
  getConnection: profile => ipcRenderer.invoke('rayovin:connection', profile),
  revalidateConnection: () => ipcRenderer.invoke('rayovin:connection:revalidate'),
  touchBackend: profile => ipcRenderer.invoke('rayovin:backend:touch', profile),
  getGatewayWsUrl: profile => ipcRenderer.invoke('rayovin:gateway:ws-url', profile),
  openSessionWindow: (sessionId, opts) => ipcRenderer.invoke('rayovin:window:openSession', sessionId, opts),
  openNewSessionWindow: () => ipcRenderer.invoke('rayovin:window:openNewSession'),
  petOverlay: {
    // Main renderer → main process: window lifecycle + drag. `request` is
    // `{ bounds, screen }`; resolves with the screen bounds it actually used.
    open: request => ipcRenderer.invoke('rayovin:pet-overlay:open', request),
    close: () => ipcRenderer.invoke('rayovin:pet-overlay:close'),
    setBounds: bounds => ipcRenderer.send('rayovin:pet-overlay:set-bounds', bounds),
    setIgnoreMouse: ignore => ipcRenderer.send('rayovin:pet-overlay:ignore-mouse', ignore),
    // Flip the overlay focusable (and focus it) while the composer needs keys.
    setFocusable: focusable => ipcRenderer.send('rayovin:pet-overlay:set-focusable', focusable),
    // Main renderer → overlay (forwarded by main): push the latest pet state.
    pushState: payload => ipcRenderer.send('rayovin:pet-overlay:state', payload),
    // Overlay → main renderer (forwarded by main): pop back in / composer submit.
    control: payload => ipcRenderer.send('rayovin:pet-overlay:control', payload),
    // Overlay subscribes to state pushes.
    onState: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('rayovin:pet-overlay:state', listener)

      return () => ipcRenderer.removeListener('rayovin:pet-overlay:state', listener)
    },
    // Main renderer subscribes to overlay control messages.
    onControl: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('rayovin:pet-overlay:control', listener)

      return () => ipcRenderer.removeListener('rayovin:pet-overlay:control', listener)
    }
  },
  getBootProgress: () => ipcRenderer.invoke('rayovin:boot-progress:get'),
  getConnectionConfig: profile => ipcRenderer.invoke('rayovin:connection-config:get', profile),
  saveConnectionConfig: payload => ipcRenderer.invoke('rayovin:connection-config:save', payload),
  applyConnectionConfig: payload => ipcRenderer.invoke('rayovin:connection-config:apply', payload),
  testConnectionConfig: payload => ipcRenderer.invoke('rayovin:connection-config:test', payload),
  probeConnectionConfig: remoteUrl => ipcRenderer.invoke('rayovin:connection-config:probe', remoteUrl),
  oauthLoginConnectionConfig: remoteUrl => ipcRenderer.invoke('rayovin:connection-config:oauth-login', remoteUrl),
  oauthLogoutConnectionConfig: remoteUrl => ipcRenderer.invoke('rayovin:connection-config:oauth-logout', remoteUrl),
  // Rayovin Cloud: one portal login powers discovery + silent per-agent sign-in
  // (cloud-auto-discovery Phase 3).
  cloud: {
    status: () => ipcRenderer.invoke('rayovin:cloud:status'),
    login: () => ipcRenderer.invoke('rayovin:cloud:login'),
    logout: () => ipcRenderer.invoke('rayovin:cloud:logout'),
    discover: org => ipcRenderer.invoke('rayovin:cloud:discover', org),
    agentSignIn: dashboardUrl => ipcRenderer.invoke('rayovin:cloud:agent-sign-in', dashboardUrl)
  },
  profile: {
    get: () => ipcRenderer.invoke('rayovin:profile:get'),
    set: name => ipcRenderer.invoke('rayovin:profile:set', name)
  },
  api: request => ipcRenderer.invoke('rayovin:api', request),
  notify: payload => ipcRenderer.invoke('rayovin:notify', payload),
  requestMicrophoneAccess: () => ipcRenderer.invoke('rayovin:requestMicrophoneAccess'),
  readFileDataUrl: filePath => ipcRenderer.invoke('rayovin:readFileDataUrl', filePath),
  readFileText: filePath => ipcRenderer.invoke('rayovin:readFileText', filePath),
  selectPaths: options => ipcRenderer.invoke('rayovin:selectPaths', options),
  writeClipboard: text => ipcRenderer.invoke('rayovin:writeClipboard', text),
  saveImageFromUrl: url => ipcRenderer.invoke('rayovin:saveImageFromUrl', url),
  saveImageBuffer: (data, ext) => ipcRenderer.invoke('rayovin:saveImageBuffer', { data, ext }),
  saveClipboardImage: () => ipcRenderer.invoke('rayovin:saveClipboardImage'),
  getPathForFile: file => {
    try {
      return webUtils.getPathForFile(file) || ''
    } catch {
      return ''
    }
  },
  normalizePreviewTarget: (target, baseDir) => ipcRenderer.invoke('rayovin:normalizePreviewTarget', target, baseDir),
  watchPreviewFile: url => ipcRenderer.invoke('rayovin:watchPreviewFile', url),
  stopPreviewFileWatch: id => ipcRenderer.invoke('rayovin:stopPreviewFileWatch', id),
  setTitleBarTheme: payload => ipcRenderer.send('rayovin:titlebar-theme', payload),
  setNativeTheme: mode => ipcRenderer.send('rayovin:native-theme', mode),
  setTranslucency: payload => ipcRenderer.send('rayovin:translucency', payload),
  setPreviewShortcutActive: active => ipcRenderer.send('rayovin:previewShortcutActive', Boolean(active)),
  openExternal: url => ipcRenderer.invoke('rayovin:openExternal', url),
  openPreviewInBrowser: url => ipcRenderer.invoke('rayovin:openPreviewInBrowser', url),
  fetchLinkTitle: url => ipcRenderer.invoke('rayovin:fetchLinkTitle', url),
  sanitizeWorkspaceCwd: cwd => ipcRenderer.invoke('rayovin:workspace:sanitize', cwd),
  settings: {
    getDefaultProjectDir: () => ipcRenderer.invoke('rayovin:setting:defaultProjectDir:get'),
    setDefaultProjectDir: dir => ipcRenderer.invoke('rayovin:setting:defaultProjectDir:set', dir),
    pickDefaultProjectDir: () => ipcRenderer.invoke('rayovin:setting:defaultProjectDir:pick')
  },
  zoom: {
    // Current zoom of this window, as { level, percent }.
    get: () => ipcRenderer.invoke('rayovin:zoom:get'),
    setPercent: percent => ipcRenderer.send('rayovin:zoom:set-percent', percent),
    // Fires on every zoom change, including the Ctrl/Cmd +/-/0 shortcuts,
    // so the settings UI can stay in sync with the keyboard.
    onChanged: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('rayovin:zoom:changed', listener)

      return () => ipcRenderer.removeListener('rayovin:zoom:changed', listener)
    }
  },
  revealLogs: () => ipcRenderer.invoke('rayovin:logs:reveal'),
  getRecentLogs: () => ipcRenderer.invoke('rayovin:logs:recent'),
  readDir: dirPath => ipcRenderer.invoke('rayovin:fs:readDir', dirPath),
  gitRoot: startPath => ipcRenderer.invoke('rayovin:fs:gitRoot', startPath),
  revealPath: targetPath => ipcRenderer.invoke('rayovin:fs:reveal', targetPath),
  openDir: dirPath => ipcRenderer.invoke('rayovin:fs:openDir', dirPath),
  renamePath: (targetPath, newName) => ipcRenderer.invoke('rayovin:fs:rename', targetPath, newName),
  writeTextFile: (filePath, content) => ipcRenderer.invoke('rayovin:fs:writeText', filePath, content),
  trashPath: targetPath => ipcRenderer.invoke('rayovin:fs:trash', targetPath),
  git: {
    worktreeList: repoPath => ipcRenderer.invoke('rayovin:git:worktreeList', repoPath),
    worktreeAdd: (repoPath, options) => ipcRenderer.invoke('rayovin:git:worktreeAdd', repoPath, options),
    worktreeRemove: (repoPath, worktreePath, options) =>
      ipcRenderer.invoke('rayovin:git:worktreeRemove', repoPath, worktreePath, options),
    branchSwitch: (repoPath, branch) => ipcRenderer.invoke('rayovin:git:branchSwitch', repoPath, branch),
    branchList: repoPath => ipcRenderer.invoke('rayovin:git:branchList', repoPath),
    baseBranchList: repoPath => ipcRenderer.invoke('rayovin:git:baseBranchList', repoPath),
    repoStatus: repoPath => ipcRenderer.invoke('rayovin:git:repoStatus', repoPath),
    fileDiff: (repoPath, filePath) => ipcRenderer.invoke('rayovin:git:fileDiff', repoPath, filePath),
    scanRepos: (roots, options) => ipcRenderer.invoke('rayovin:git:scanRepos', roots, options),
    review: {
      list: (repoPath, scope, baseRef) => ipcRenderer.invoke('rayovin:git:review:list', repoPath, scope, baseRef),
      diff: (repoPath, filePath, scope, baseRef, staged) =>
        ipcRenderer.invoke('rayovin:git:review:diff', repoPath, filePath, scope, baseRef, staged),
      stage: (repoPath, filePath) => ipcRenderer.invoke('rayovin:git:review:stage', repoPath, filePath),
      unstage: (repoPath, filePath) => ipcRenderer.invoke('rayovin:git:review:unstage', repoPath, filePath),
      revert: (repoPath, filePath) => ipcRenderer.invoke('rayovin:git:review:revert', repoPath, filePath),
      revParse: (repoPath, ref) => ipcRenderer.invoke('rayovin:git:review:revParse', repoPath, ref),
      commit: (repoPath, message, push) => ipcRenderer.invoke('rayovin:git:review:commit', repoPath, message, push),
      commitContext: repoPath => ipcRenderer.invoke('rayovin:git:review:commitContext', repoPath),
      push: repoPath => ipcRenderer.invoke('rayovin:git:review:push', repoPath),
      shipInfo: repoPath => ipcRenderer.invoke('rayovin:git:review:shipInfo', repoPath),
      createPr: repoPath => ipcRenderer.invoke('rayovin:git:review:createPr', repoPath)
    }
  },
  terminal: {
    cwd: id => ipcRenderer.invoke('rayovin:terminal:cwd', id),
    dispose: id => ipcRenderer.invoke('rayovin:terminal:dispose', id),
    resize: (id, size) => ipcRenderer.invoke('rayovin:terminal:resize', id, size),
    start: options => ipcRenderer.invoke('rayovin:terminal:start', options),
    write: (id, data) => ipcRenderer.invoke('rayovin:terminal:write', id, data),
    onData: (id, callback) => {
      const channel = `rayovin:terminal:${id}:data`
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on(channel, listener)

      return () => ipcRenderer.removeListener(channel, listener)
    },
    onExit: (id, callback) => {
      const channel = `rayovin:terminal:${id}:exit`
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on(channel, listener)

      return () => ipcRenderer.removeListener(channel, listener)
    }
  },
  onClosePreviewRequested: callback => {
    const listener = () => callback()
    ipcRenderer.on('rayovin:close-preview-requested', listener)

    return () => ipcRenderer.removeListener('rayovin:close-preview-requested', listener)
  },
  onOpenUpdatesRequested: callback => {
    const listener = () => callback()
    ipcRenderer.on('rayovin:open-updates', listener)

    return () => ipcRenderer.removeListener('rayovin:open-updates', listener)
  },
  onDeepLink: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('rayovin:deep-link', listener)

    return () => ipcRenderer.removeListener('rayovin:deep-link', listener)
  },
  signalDeepLinkReady: () => ipcRenderer.invoke('rayovin:deep-link-ready'),
  onWindowStateChanged: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('rayovin:window-state-changed', listener)

    return () => ipcRenderer.removeListener('rayovin:window-state-changed', listener)
  },
  onFocusSession: callback => {
    const listener = (_event, sessionId) => callback(sessionId)
    ipcRenderer.on('rayovin:focus-session', listener)

    return () => ipcRenderer.removeListener('rayovin:focus-session', listener)
  },
  onNotificationAction: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('rayovin:notification-action', listener)

    return () => ipcRenderer.removeListener('rayovin:notification-action', listener)
  },
  onPreviewFileChanged: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('rayovin:preview-file-changed', listener)

    return () => ipcRenderer.removeListener('rayovin:preview-file-changed', listener)
  },
  onBackendExit: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('rayovin:backend-exit', listener)

    return () => ipcRenderer.removeListener('rayovin:backend-exit', listener)
  },
  // Soft gateway-mode apply finished tearing down the primary backend. Renderer
  // should wipe session lists + re-dial without a window reload.
  onConnectionApplied: callback => {
    const listener = () => callback()
    ipcRenderer.on('rayovin:connection:applied', listener)

    return () => ipcRenderer.removeListener('rayovin:connection:applied', listener)
  },
  onPowerResume: callback => {
    const listener = () => callback()
    ipcRenderer.on('rayovin:power-resume', listener)

    return () => ipcRenderer.removeListener('rayovin:power-resume', listener)
  },
  onBootProgress: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('rayovin:boot-progress', listener)

    return () => ipcRenderer.removeListener('rayovin:boot-progress', listener)
  },
  // First-launch bootstrap progress -- emitted by the install.ps1 stage
  // runner in main.ts (apps/desktop/electron/bootstrap-runner.ts).
  // Renderer's install overlay subscribes to live events and queries the
  // current snapshot via getBootstrapState() to recover after a devtools
  // reload mid-bootstrap.
  getBootstrapState: () => ipcRenderer.invoke('rayovin:bootstrap:get'),
  resetBootstrap: () => ipcRenderer.invoke('rayovin:bootstrap:reset'),
  repairBootstrap: () => ipcRenderer.invoke('rayovin:bootstrap:repair'),
  cancelBootstrap: () => ipcRenderer.invoke('rayovin:bootstrap:cancel'),
  onBootstrapEvent: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('rayovin:bootstrap:event', listener)

    return () => ipcRenderer.removeListener('rayovin:bootstrap:event', listener)
  },
  getVersion: () => ipcRenderer.invoke('rayovin:version'),
  getRemoteDisplayReason: () => ipcRenderer.invoke('rayovin:get-remote-display-reason'),
  uninstall: {
    summary: () => ipcRenderer.invoke('rayovin:uninstall:summary'),
    run: mode => ipcRenderer.invoke('rayovin:uninstall:run', { mode })
  },
  updates: {
    check: () => ipcRenderer.invoke('rayovin:updates:check'),
    apply: opts => ipcRenderer.invoke('rayovin:updates:apply', opts),
    getBranch: () => ipcRenderer.invoke('rayovin:updates:branch:get'),
    setBranch: name => ipcRenderer.invoke('rayovin:updates:branch:set', name),
    onProgress: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('rayovin:updates:progress', listener)

      return () => ipcRenderer.removeListener('rayovin:updates:progress', listener)
    }
  },
  themes: {
    fetchMarketplace: id => ipcRenderer.invoke('rayovin:vscode-theme:fetch', id),
    searchMarketplace: query => ipcRenderer.invoke('rayovin:vscode-theme:search', query)
  }
})
