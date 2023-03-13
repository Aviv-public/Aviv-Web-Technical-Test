module.exports = {
  root: true,
  extends: ['react-app', 'eslint:recommended', 'plugin:prettier/recommended'],
  plugins: ['prettier', 'simple-import-sort'],
  rules: {
    'prettier/prettier': 'error',
    'simple-import-sort/imports': [
      'error',
      {
        groups: [
          // Side effect imports
          ['^\\u0000'],
          // Node.js builtins. You could also generate this regex if you use a `.js` config.
          // For example: `^(${require("module").builtinModules.join("|")})(/|$)`
          [
            '^(assert|buffer|child_process|cluster|console|crypto|dgram|dns|domain|events|fs|http|https|module|net|os|path|punycode|querystring|readline|repl|stream|string_decoder|sys|timers|tls|tty|url|util|vm|zlib|freelist|v8|process|async_hooks|http2|perf_hooks)(/.*|$)',
          ],
          // Packages. `react` related packages come first.
          ['^react$', '^@?\\w'],
          // Internal imports. This package doesn't manage absolute imports for now
          [
            '^(app|components|containers|enums|constants|custom-hooks|fonts|images|helpers|pdf|propTypes|services|sagas|sass|test-fixtures|test-helpers|types|setupTests)(/.*|$)',
          ],
          // Parent imports. Put `..` last.
          ['^\\.\\.(?!/?$)', '^\\.\\./?$'],
          // Other relative imports. Put same-folder imports and `.` last.
          ['^\\./(?=.*/)(?!/?$)', '^\\.(?!/?$)', '^\\./?$'],
          // Style imports.
          ['^.+\\.s?css$'],
        ],
      },
    ],
  },
  globals: {
    JSX: 'readonly',
  },
};
