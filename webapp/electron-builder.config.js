if (process.env.VITE_APP_VERSION === undefined) {
  const now = new Date;
  process.env.VITE_APP_VERSION = `${now.getUTCFullYear() - 2000}.${now.getUTCMonth() + 1}.${now.getUTCDate()}-${now.getUTCHours() * 60 + now.getUTCMinutes()}`;
}

/**
 * @type {import('electron-builder').Configuration}
 * @see https://www.electron.build/configuration/configuration
 */
const config = {
  appId: 'com.ealyce.alas-ce',
  productName: 'Alas CE',
  directories: {
    output: 'dist',
    buildResources: 'buildResources',
  },
  files: [
    'packages/**/dist/**',
  ],
  extraMetadata: {
    version: process.env.VITE_APP_VERSION,
  },
  win: {
    icon: 'buildResources/icon.ico',
    target: 'nsis',
  },
  mac: {
    icon: 'buildResources/icon.icns',
    target: 'dmg',
  },
  linux: {
    icon: 'buildResources/icon.png',
    target: 'AppImage',
  },
};

module.exports = config;
