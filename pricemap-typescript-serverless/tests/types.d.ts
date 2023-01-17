export {};

// To ignore DOM related types
// used by Vitest
declare global {
  interface Worker {}
  class EventTarget {}
  interface AddEventListenerOptions {}
  interface EventListenerOptions {}
  interface Event {}
  namespace WebAssembly {
    interface Module {}
  }
}
