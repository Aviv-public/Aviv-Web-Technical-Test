module.exports = {
  root: true,
  extends: ['react-app', 'eslint:recommended', 'plugin:prettier/recommended'],
  plugins: ['prettier'],
  rules: {
    'prettier/prettier': 'error',
  },
  globals: {
    JSX: 'readonly',
  },
};
