/**
 * @license
 * Copyright 2015 Bodymovin
 * SPDX-License-Identifier: MIT
 */

/**
 * @license
 * Copyright 2014-2015, Epistemex by Ken Fyrstenberg and contributions by
 * leeoniya SPDX-License-Identifier: MIT
 */

/**
 * @license
 * Copyright 2014 David Bau
 * SPDX-License-Identifier: MIT
 */

/**
 * @license
 * Copyright 2014 - 2015, BezierEasing by Gaëtan Renaudeau
 * SPDX-License-Identifier: MIT
 */

(typeof navigator !== 'undefined') && (function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    define(function() {
      return factory(root);
    });
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory(root);
  } else {
    root.lottie = factory(root);
    root.bodymovin = root.lottie;
  }
}((window || {}), function(window) {
  'use strict';
  var h, e = 'http://www.w3.org/2000/svg', A = '', s = -999999, i = !0,
         n = /^((?!chrome|android).)*safari/i.test(navigator.userAgent),
         _ = Math.pow, k = Math.sqrt, f = Math.floor, d = (Math.max, Math.min),
         a = {};
  !function() {
    var t,
        e =
            [
              'abs',   'acos',  'acosh',  'asin',  'asinh',  'atan',
              'atanh', 'atan2', 'ceil',   'cbrt',  'expm1',  'clz32',
              'cos',   'cosh',  'exp',    'floor', 'fround', 'hypot',
              'imul',  'log',   'log1p',  'log2',  'log10',  'max',
              'min',   'pow',   'random', 'round', 'sign',   'sin',
              'sinh',  'sqrt',  'tan',    'tanh',  'trunc',  'E',
              'LN10',  'LN2',   'LOG10E', 'LOG2E', 'PI',     'SQRT1_2',
              'SQRT2'
            ],
        s = e.length;
    for (t = 0; t < s; t += 1) a[e[t]] = Math[e[t]]
  }(),
      a.random = Math.random, a.abs = function(t) {
        if ('object' === typeof t && t.length) {
          var e, s = D(t.length), i = t.length;
          for (e = 0; e < i; e += 1) s[e] = Math.abs(t[e]);
          return s
        }
        return Math.abs(t)
      };
  var P = 150, B = Math.PI / 180, v = .5519;
  function r(t) {
    t ? Math.round : function(t) {
      return t
    }
  }
  function o(t, e, s, i) {
    this.type = t, this.currentTime = e, this.totalTime = s,
    this.direction = i < 0 ? -1 : 1
  }
  function l(t, e) {
    this.type = t, this.direction = e < 0 ? -1 : 1
  }
  function p(t, e, s, i) {
    this.type = t, this.currentLoop = s, this.totalLoops = e,
    this.direction = i < 0 ? -1 : 1
  }
  function m(t, e, s) {
    this.type = t, this.firstFrame = e, this.totalFrames = s
  }
  function c(t, e) {
    this.type = t, this.target = e
  }
  function u(t, e) {
    this.type = 'renderFrameError', this.nativeError = t, this.currentTime = e
  }
  function g(t) {
    this.type = 'configError', this.nativeError = t
  }
  r(!1);
  var t, S = (t = 0, function() {
           return '__lottie_element_' + (t += 1)
         });
  function y(t, e, s) {
    var i, a, r, n, h, o, l, p;
    switch (o = s * (1 - e),
            l = s * (1 - (h = 6 * t - (n = Math.floor(6 * t))) * e),
            p = s * (1 - (1 - h) * e), n % 6) {
      case 0:
        i = s, a = p, r = o;
        break;
      case 1:
        i = l, a = s, r = o;
        break;
      case 2:
        i = o, a = s, r = p;
        break;
      case 3:
        i = o, a = l, r = s;
        break;
      case 4:
        i = p, a = o, r = s;
        break;
      case 5:
        i = s, a = o, r = l
    }
    return [i, a, r]
  }
  function b(t, e, s) {
    var i, a = Math.max(t, e, s), r = Math.min(t, e, s), n = a - r,
           h = 0 === a ? 0 : n / a, o = a / 255;
    switch (a) {
      case r:
        i = 0;
        break;
      case t:
        i = e - s + n * (e < s ? 6 : 0), i /= 6 * n;
        break;
      case e:
        i = s - t + 2 * n, i /= 6 * n;
        break;
      case s:
        i = t - e + 4 * n, i /= 6 * n
    }
    return [i, h, o]
  }
  function lt(t, e) {
    var s = b(255 * t[0], 255 * t[1], 255 * t[2]);
    return s[1] += e, 1 < s[1] ? s[1] = 1 : s[1] <= 0 && (s[1] = 0),
                                 y(s[0], s[1], s[2])
  }
  function pt(t, e) {
    var s = b(255 * t[0], 255 * t[1], 255 * t[2]);
    return s[2] += e, 1 < s[2] ? s[2] = 1 : s[2] < 0 && (s[2] = 0),
                                 y(s[0], s[1], s[2])
  }
  function ft(t, e) {
    var s = b(255 * t[0], 255 * t[1], 255 * t[2]);
    return s[0] += e / 360, 1 < s[0] ? s[0] -= 1 : s[0] < 0 && (s[0] += 1),
           y(s[0], s[1], s[2])
  }
  !function() {
    var t, e, s = [];
    for (t = 0; t < 256; t += 1)
      e = t.toString(16), s[t] = 1 === e.length ? '0' + e : e
  }();
  function C() {}
  C.prototype = {
    triggerEvent: function(t, e) {
      if (this._cbs[t])
        for (var s = this._cbs[t].length, i = 0; i < s; i += 1)
          this._cbs[t][i](e)
    },
    addEventListener: function(t, e) {
      return this._cbs[t] || (this._cbs[t] = []), this._cbs[t].push(e),
             function() {
               this.removeEventListener(t, e)
             }.bind(this)
    },
    removeEventListener: function(t, e) {
      if (e) {
        if (this._cbs[t]) {
          for (var s = 0, i = this._cbs[t].length; s < i;)
            this._cbs[t][s] === e &&
                (this._cbs[t].splice(s, 1), s -= 1, i -= 1),
                s += 1;
          this._cbs[t].length || (this._cbs[t] = null)
        }
      } else
        this._cbs[t] = null
    }
  };
  var j = function() {
    function s(t, e) {
      var s, i = 0, a = [];
      switch (t) {
        case 'int16':
        case 'uint8c':
          s = 1;
          break;
        default:
          s = 1.1
      }
      for (i = 0; i < e; i += 1) a.push(s);
      return a
    }
    return 'function' == typeof Uint8ClampedArray &&
            'function' == typeof Float32Array ?
        function(t, e) {
          return 'float32' === t ? new Float32Array(e) :
              'int16' === t      ? new Int16Array(e) :
              'uint8c' === t     ? new Uint8ClampedArray(e) :
                                   s(t, e)
        } :
        s
  }();
  function D(t) {
    return Array.apply(null, {length: t})
  }
  function x(t) {
    return document.createElementNS(e, t)
  }
  function w(t) {
    return document.createElement(t)
  }
  function F() {}
  F.prototype = {
    addDynamicProperty: function(t) {
      -1 === this.dynamicProperties.indexOf(t) &&
          (this.dynamicProperties.push(t),
           this.container.addDynamicProperty(this), this._isAnimated = !0)
    },
    iterateDynamicProperties: function() {
      var t;
      this._mdf = !1;
      var e = this.dynamicProperties.length;
      for (t = 0; t < e; t += 1)
        this.dynamicProperties[t].getValue(),
            this.dynamicProperties[t]._mdf && (this._mdf = !0)
    },
    initDynamicPropertyContainer: function(t) {
      this.container = t, this.dynamicProperties = [], this._mdf = !1,
      this._isAnimated = !1
    }
  };
  var T,
      E =
          (T = {
            0: 'source-over',
            1: 'multiply',
            2: 'screen',
            3: 'overlay',
            4: 'darken',
            5: 'lighten',
            6: 'color-dodge',
            7: 'color-burn',
            8: 'hard-light',
            9: 'soft-light',
            10: 'difference',
            11: 'exclusion',
            12: 'hue',
            13: 'saturation',
            14: 'color',
            15: 'luminosity'
          },
           function(t) {
             return T[t] || ''
           }),
      I = function() {
        var a = Math.cos, r = Math.sin, n = Math.tan, i = Math.round;
        function t() {
          return this.props[0] = 1, this.props[1] = 0, this.props[2] = 0,
                 this.props[3] = 0, this.props[4] = 0, this.props[5] = 1,
                 this.props[6] = 0, this.props[7] = 0, this.props[8] = 0,
                 this.props[9] = 0, this.props[10] = 1, this.props[11] = 0,
                 this.props[12] = 0, this.props[13] = 0, this.props[14] = 0,
                 this.props[15] = 1, this
        }
        function e(t) {
          if (0 === t) return this;
          var e = a(t), s = r(t);
          return this._t(e, -s, 0, 0, s, e, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
        }
        function s(t) {
          if (0 === t) return this;
          var e = a(t), s = r(t);
          return this._t(1, 0, 0, 0, 0, e, -s, 0, 0, s, e, 0, 0, 0, 0, 1)
        }
        function h(t) {
          if (0 === t) return this;
          var e = a(t), s = r(t);
          return this._t(e, 0, s, 0, 0, 1, 0, 0, -s, 0, e, 0, 0, 0, 0, 1)
        }
        function o(t) {
          if (0 === t) return this;
          var e = a(t), s = r(t);
          return this._t(e, -s, 0, 0, s, e, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
        }
        function l(t, e) {
          return this._t(1, e, t, 1, 0, 0)
        }
        function p(t, e) {
          return this.shear(n(t), n(e))
        }
        function f(t, e) {
          var s = a(e), i = r(e);
          return this._t(s, i, 0, 0, -i, s, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
              ._t(1, 0, 0, 0, n(t), 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
              ._t(s, -i, 0, 0, i, s, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
        }
        function d(t, e, s) {
          return s || 0 === s || (s = 1),
                 1 === t && 1 === e && 1 === s ?
                     this :
                     this._t(t, 0, 0, 0, 0, e, 0, 0, 0, 0, s, 0, 0, 0, 0, 1)
        }
        function m(t, e, s, i, a, r, n, h, o, l, p, f, d, m, c, u) {
          return this.props[0] = t, this.props[1] = e, this.props[2] = s,
                 this.props[3] = i, this.props[4] = a, this.props[5] = r,
                 this.props[6] = n, this.props[7] = h, this.props[8] = o,
                 this.props[9] = l, this.props[10] = p, this.props[11] = f,
                 this.props[12] = d, this.props[13] = m, this.props[14] = c,
                 this.props[15] = u, this
        }
        function c(t, e, s) {
          return s = s || 0,
                 0 !== t || 0 !== e || 0 !== s ?
                     this._t(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, t, e, s, 1) :
                     this
        }
        function u(t, e, s, i, a, r, n, h, o, l, p, f, d, m, c, u) {
          var g = this.props;
          if (1 === t && 0 === e && 0 === s && 0 === i && 0 === a && 1 === r &&
              0 === n && 0 === h && 0 === o && 0 === l && 1 === p && 0 === f)
            return g[12] = g[12] * t + g[15] * d, g[13] = g[13] * r + g[15] * m,
                   g[14] = g[14] * p + g[15] * c, g[15] *= u,
                   this._identityCalculated = !1, this;
          var y = g[0], v = g[1], b = g[2], _ = g[3], k = g[4], A = g[5],
              P = g[6], S = g[7], C = g[8], D = g[9], x = g[10], w = g[11],
              F = g[12], T = g[13], E = g[14], M = g[15];
          return g[0] = y * t + v * a + b * o + _ * d,
                 g[1] = y * e + v * r + b * l + _ * m,
                 g[2] = y * s + v * n + b * p + _ * c,
                 g[3] = y * i + v * h + b * f + _ * u,
                 g[4] = k * t + A * a + P * o + S * d,
                 g[5] = k * e + A * r + P * l + S * m,
                 g[6] = k * s + A * n + P * p + S * c,
                 g[7] = k * i + A * h + P * f + S * u,
                 g[8] = C * t + D * a + x * o + w * d,
                 g[9] = C * e + D * r + x * l + w * m,
                 g[10] = C * s + D * n + x * p + w * c,
                 g[11] = C * i + D * h + x * f + w * u,
                 g[12] = F * t + T * a + E * o + M * d,
                 g[13] = F * e + T * r + E * l + M * m,
                 g[14] = F * s + T * n + E * p + M * c,
                 g[15] = F * i + T * h + E * f + M * u,
                 this._identityCalculated = !1, this
        }
        function g() {
          return this._identityCalculated ||
                     (this._identity =
                          !(1 !== this.props[0] || 0 !== this.props[1] ||
                            0 !== this.props[2] || 0 !== this.props[3] ||
                            0 !== this.props[4] || 1 !== this.props[5] ||
                            0 !== this.props[6] || 0 !== this.props[7] ||
                            0 !== this.props[8] || 0 !== this.props[9] ||
                            1 !== this.props[10] || 0 !== this.props[11] ||
                            0 !== this.props[12] || 0 !== this.props[13] ||
                            0 !== this.props[14] || 1 !== this.props[15]),
                      this._identityCalculated = !0),
                 this._identity
        }
        function y(t) {
          for (var e = 0; e < 16;) {
            if (t.props[e] !== this.props[e]) return !1;
            e += 1
          }
          return !0
        }
        function v(t) {
          var e;
          for (e = 0; e < 16; e += 1) t.props[e] = this.props[e];
          return t
        }
        function b(t) {
          var e;
          for (e = 0; e < 16; e += 1) this.props[e] = t[e]
        }
        function _(t, e, s) {
          return {
            x: t * this.props[0] + e * this.props[4] + s * this.props[8] +
                this.props[12],
                y: t * this.props[1] + e * this.props[5] + s * this.props[9] +
                this.props[13],
                z: t * this.props[2] + e * this.props[6] + s * this.props[10] +
                this.props[14]
          }
        }
        function k(t, e, s) {
          return t * this.props[0] + e * this.props[4] + s * this.props[8] +
              this.props[12]
        }
        function A(t, e, s) {
          return t * this.props[1] + e * this.props[5] + s * this.props[9] +
              this.props[13]
        }
        function P(t, e, s) {
          return t * this.props[2] + e * this.props[6] + s * this.props[10] +
              this.props[14]
        }
        function S() {
          var t = this.props[0] * this.props[5] - this.props[1] * this.props[4],
              e = this.props[5] / t, s = -this.props[1] / t,
              i = -this.props[4] / t, a = this.props[0] / t,
              r = (this.props[4] * this.props[13] -
                   this.props[5] * this.props[12]) /
              t,
              n = -(this.props[0] * this.props[13] -
                    this.props[1] * this.props[12]) /
              t,
              h = new I;
          return h.props[0] = e, h.props[1] = s, h.props[4] = i, h.props[5] = a,
                 h.props[12] = r, h.props[13] = n, h
        }
        function C(t) {
          return this.getInverseMatrix().applyToPointArray(
              t[0], t[1], t[2] || 0)
        }
        function D(t) {
          var e, s = t.length, i = [];
          for (e = 0; e < s; e += 1) i[e] = C(t[e]);
          return i
        }
        function x(t, e, s) {
          var i = j('float32', 6);
          if (this.isIdentity())
            i[0] = t[0], i[1] = t[1], i[2] = e[0], i[3] = e[1], i[4] = s[0],
            i[5] = s[1];
          else {
            var a = this.props[0], r = this.props[1], n = this.props[4],
                h = this.props[5], o = this.props[12], l = this.props[13];
            i[0] = t[0] * a + t[1] * n + o, i[1] = t[0] * r + t[1] * h + l,
            i[2] = e[0] * a + e[1] * n + o, i[3] = e[0] * r + e[1] * h + l,
            i[4] = s[0] * a + s[1] * n + o, i[5] = s[0] * r + s[1] * h + l
          }
          return i
        }
        function w(t, e, s) {
          return this.isIdentity() ? [t, e, s] : [
            t * this.props[0] + e * this.props[4] + s * this.props[8] +
                this.props[12],
            t * this.props[1] + e * this.props[5] + s * this.props[9] +
                this.props[13],
            t * this.props[2] + e * this.props[6] + s * this.props[10] +
                this.props[14]
          ]
        }
        function F(t, e) {
          if (this.isIdentity()) return t + ',' + e;
          var s = this.props;
          return Math.round(100 * (t * s[0] + e * s[4] + s[12])) / 100 + ',' +
              Math.round(100 * (t * s[1] + e * s[5] + s[13])) / 100
        }
        function T() {
          for (var t = 0, e = this.props, s = 'matrix3d('; t < 16;)
            s += i(1e4 * e[t]) / 1e4, s += 15 === t ? ')' : ',', t += 1;
          return s
        }
        function E(t) {
          return t < 1e-6 && 0 < t || -1e-6 < t && t < 0 ? i(1e4 * t) / 1e4 : t
        }
        function M() {
          var t = this.props;
          return 'matrix(' + E(t[0]) + ',' + E(t[1]) + ',' + E(t[4]) + ',' +
              E(t[5]) + ',' + E(t[12]) + ',' + E(t[13]) + ')'
        }
        return function() {
          this.reset = t, this.rotate = e, this.rotateX = s, this.rotateY = h,
          this.rotateZ = o, this.skew = p, this.skewFromAxis = f,
          this.shear = l, this.scale = d, this.setTransform = m,
          this.translate = c, this.transform = u, this.applyToPoint = _,
          this.applyToX = k, this.applyToY = A, this.applyToZ = P,
          this.applyToPointArray = w, this.applyToTriplePoints = x,
          this.applyToPointStringified = F, this.toCSS = T, this.to2dCSS = M,
          this.clone = v, this.cloneFromProps = b, this.equals = y,
          this.inversePoints = D, this.inversePoint = C,
          this.getInverseMatrix = S, this._t = this.transform,
          this.isIdentity = g, this._identity = !0,
          this._identityCalculated = !1, this.props = j('float32', 16),
          this.reset()
        }
      }();
  !function(h, o) {
    var l, p = this, f = 256, d = 6, m = 'random', c = o.pow(f, d),
           u = o.pow(2, 52), g = 2 * u, y = f - 1;
    function v(t) {
      var e, s = t.length, n = this, i = 0, a = n.i = n.j = 0, r = n.S = [];
      for (s || (t = [s++]); i < f;) r[i] = i++;
      for (i = 0; i < f; i++)
        r[i] = r[a = y & a + t[i % s] + (e = r[i])], r[a] = e;
      n.g = function(t) {
        for (var e, s = 0, i = n.i, a = n.j, r = n.S; t--;)
          e = r[i = y & i + 1],
          s = s * f + r[y & (r[i] = r[a = y & a + e]) + (r[a] = e)];
        return n.i = i, n.j = a, s
      }
    }
    function b(t, e) {
      return e.i = t.i, e.j = t.j, e.S = t.S.slice(), e
    }
    function _(t, e) {
      for (var s, i = t + '', a = 0; a < i.length;)
        e[y & a] = y & (s ^= 19 * e[y & a]) + i.charCodeAt(a++);
      return k(e)
    }
    function k(t) {
      return String.fromCharCode.apply(0, t)
    }
    o['seed' + m] = function(t, e, s) {
      var i = [],
          a = _(
              function t(e, s) {
                var i, a = [], r = typeof e;
                if (s && 'object' == r)
                  for (i in e) try {
                      a.push(t(e[i], s - 1))
                    } catch (t) {
                    }
                return a.length ? a : 'string' == r ? e : e + '\0'
              }((e = !0 === e ? {entropy: !0} : e || {}).entropy ?
                    [t, k(h)] :
                    null === t ?
                    function() {
                      try {
                        if (l) return k(l.randomBytes(f));
                        var t = new Uint8Array(f);
                        return (p.crypto || p.msCrypto).getRandomValues(t), k(t)
                      } catch (t) {
                        var e = p.navigator, s = e && e.plugins;
                        return [+new Date, p, s, p.screen, k(h)]
                      }
                    }() :
                    t,
                3),
              i),
          r = new v(i), n = function() {
            for (var t = r.g(d), e = c, s = 0; t < u;)
              t = (t + s) * f, e *= f, s = r.g(1);
            for (; g <= t;) t /= 2, e /= 2, s >>>= 1;
            return (t + s) / e
          };
      return n.int32 = function() {
        return 0 | r.g(4)
      }, n.quick = function() {
        return r.g(4) / 4294967296
      }, n.double = n, _(k(r.S), h), (e.pass || s || function(t, e, s, i) {
               return i && (i.S && b(i, r), t.state = function() {
                        return b(r, {})
                      }), s ? (o[m] = t, e) : t
             })(n, a, 'global' in e ? e.global : this == o, e.state)
    }, _(o.random(), h)
  }([], a);
  var W = function() {
    var t = {
      getBezierEasing: function(t, e, s, i, a) {
        var r =
            a || ('bez_' + t + '_' + e + '_' + s + '_' + i).replace(/\./g, 'p');
        if (h[r]) return h[r];
        var n = new o([t, e, s, i]);
        return h[r] = n
      }
    },
        h = {};
    var l = 11, p = 1 / (l - 1), e = 'function' == typeof Float32Array;
    function i(t, e) {
      return 1 - 3 * e + 3 * t
    }
    function a(t, e) {
      return 3 * e - 6 * t
    }
    function r(t) {
      return 3 * t
    }
    function f(t, e, s) {
      return ((i(e, s) * t + a(e, s)) * t + r(e)) * t
    }
    function d(t, e, s) {
      return 3 * i(e, s) * t * t + 2 * a(e, s) * t + r(e)
    }
    function o(t) {
      this._p = t, this._mSampleValues = e ? new Float32Array(l) : new Array(l),
      this._precomputed = !1, this.get = this.get.bind(this)
    }
    return o.prototype = {
      get: function(t) {
        var e = this._p[0], s = this._p[1], i = this._p[2], a = this._p[3];
        return this._precomputed || this._precompute(),
               e === s && i === a ? t :
                   0 === t        ? 0 :
                   1 === t        ? 1 :
                                    f(this._getTForX(t), s, a)
      },
             _precompute: function() {
        var t = this._p[0], e = this._p[1], s = this._p[2], i = this._p[3];
        this._precomputed = !0, t === e && s === i || this._calcSampleValues()
      },
      _calcSampleValues: function() {
        for (var t = this._p[0], e = this._p[2], s = 0; s < l; ++s)
          this._mSampleValues[s] = f(s * p, t, e)
      },
      _getTForX: function(t) {
        for (var e = this._p[0], s = this._p[2], i = this._mSampleValues, a = 0,
                 r = 1, n = l - 1;
             r !== n && i[r] <= t; ++r)
          a += p;
        var h = a + (t - i[--r]) / (i[r + 1] - i[r]) * p, o = d(h, e, s);
        return .001 <= o ?
            function(t, e, s, i) {
              for (var a = 0; a < 4; ++a) {
                var r = d(e, s, i);
                if (0 === r) return e;
                e -= (f(e, s, i) - t) / r
              }
              return e
            }(t, h, e, s) :
            0 === o ?
            h :
            function(t, e, s, i, a) {
              for (var r, n, h = 0;
                   0 < (r = f(n = e + (s - e) / 2, i, a) - t) ? s = n : e = n,
                             1e-7 < Math.abs(r) && ++h < 10;);
              return n
            }(t, a, a + p, e, s)
      }
    },
           t
  }();
  function M(t, e) {
    var s, i, a = t.length;
    for (s = 0; s < a; s += 1)
      for (var r in i = t[s].prototype)
        Object.prototype.hasOwnProperty.call(i, r) && (e.prototype[r] = i[r])
  }
  !function() {
    for (var a = 0, t = ['ms', 'moz', 'webkit', 'o'], e = 0;
         e < t.length && !window.requestAnimationFrame; ++e)
      window.requestAnimationFrame = window[t[e] + 'RequestAnimationFrame'],
      window.cancelAnimationFrame = window[t[e] + 'CancelAnimationFrame'] ||
          window[t[e] + 'CancelRequestAnimationFrame'];
    window.requestAnimationFrame ||
        (window.requestAnimationFrame =
             function(t) {
               var e = (new Date).getTime(), s = Math.max(0, 16 - (e - a)),
                   i = setTimeout(function() {
                     t(e + s)
                   }, s);
               return a = e + s, i
             }),
        window.cancelAnimationFrame ||
        (window.cancelAnimationFrame = function(t) {
          clearTimeout(t)
        })
  }();
  var dt = function() {
    var F = Math;
    function g(t, e, s, i, a, r) {
      var n = t * i + e * a + s * r - a * i - r * t - s * e;
      return -.001 < n && n < .001
    }
    var p = function(t, e, s, i) {
      var a, r, n, h, o, l, p = P, f = 0, d = [], m = [], c = Ft.newElement();
      for (n = s.length, a = 0; a < p; a += 1) {
        for (o = a / (p - 1), r = l = 0; r < n; r += 1)
          h = _(1 - o, 3) * t[r] + 3 * _(1 - o, 2) * o * s[r] +
              3 * (1 - o) * _(o, 2) * i[r] + _(o, 3) * e[r],
          d[r] = h, null !== m[r] && (l += _(d[r] - m[r], 2)), m[r] = d[r];
        l && (f += l = k(l)), c.percents[a] = o, c.lengths[a] = f
      }
      return c.addedLength = f, c
    };
    function y(t) {
      this.segmentLength = 0, this.points = new Array(t)
    }
    function v(t, e) {
      this.partialLength = t, this.point = e
    }
    var b,
        t = (b = {}, function(t, e, s, i) {
          var a = (t[0] + '_' + t[1] + '_' + e[0] + '_' + e[1] + '_' + s[0] +
                   '_' + s[1] + '_' + i[0] + '_' + i[1])
                      .replace(/\./g, 'p');
          if (!b[a]) {
            var r, n, h, o, l, p, f, d = P, m = 0, c = null;
            2 === t.length && (t[0] !== e[0] || t[1] !== e[1]) &&
                g(t[0], t[1], e[0], e[1], t[0] + s[0], t[1] + s[1]) &&
                g(t[0], t[1], e[0], e[1], e[0] + i[0], e[1] + i[1]) && (d = 2);
            var u = new y(d);
            for (h = s.length, r = 0; r < d; r += 1) {
              for (f = D(h), l = r / (d - 1), n = p = 0; n < h; n += 1)
                o = _(1 - l, 3) * t[n] + 3 * _(1 - l, 2) * l * (t[n] + s[n]) +
                    3 * (1 - l) * _(l, 2) * (e[n] + i[n]) + _(l, 3) * e[n],
                f[n] = o, null !== c && (p += _(f[n] - c[n], 2));
              m += p = k(p), u.points[r] = new v(p, f), c = f
            }
            u.segmentLength = m, b[a] = u
          }
          return b[a]
        });
    function T(t, e) {
      var s = e.percents, i = e.lengths, a = s.length, r = f((a - 1) * t),
          n = t * e.addedLength, h = 0;
      if (r === a - 1 || 0 === r || n === i[r]) return s[r];
      for (var o = i[r] > n ? -1 : 1, l = !0; l;)
        if (i[r] <= n && i[r + 1] > n ?
                (h = (n - i[r]) / (i[r + 1] - i[r]), l = !1) :
                r += o,
            r < 0 || a - 1 <= r) {
          if (r === a - 1) return s[r];
          l = !1
        }
      return s[r] + (s[r + 1] - s[r]) * h
    }
    var E = j('float32', 8);
    return {
      getSegmentsLength:
          function(t) {
            var e, s = wt.newElement(), i = t.c, a = t.v, r = t.o, n = t.i,
                   h = t._length, o = s.lengths, l = 0;
            for (e = 0; e < h - 1; e += 1)
              o[e] = p(a[e], a[e + 1], r[e], n[e + 1]), l += o[e].addedLength;
            return i && h &&
                       (o[e] = p(a[e], a[0], r[e], n[0]),
                        l += o[e].addedLength),
                   s.totalLength = l, s
          },
          getNewSegment:
              function(t, e, s, i, a, r, n) {
                a < 0 ? a = 0 : 1 < a && (a = 1);
                var h, o = T(a, n), l = T(r = 1 < r ? 1 : r, n), p = t.length,
                       f = 1 - o, d = 1 - l, m = f * f * f, c = o * f * f * 3,
                       u = o * o * f * 3, g = o * o * o, y = f * f * d,
                       v = o * f * d + f * o * d + f * f * l,
                       b = o * o * d + f * o * l + o * f * l, _ = o * o * l,
                       k = f * d * d, A = o * d * d + f * l * d + f * d * l,
                       P = o * l * d + f * l * l + o * d * l, S = o * l * l,
                       C = d * d * d, D = l * d * d + d * l * d + d * d * l,
                       x = l * l * d + d * l * l + l * d * l, w = l * l * l;
                for (h = 0; h < p; h += 1)
                  E[4 * h] =
                      F.round(
                          1e3 * (m * t[h] + c * s[h] + u * i[h] + g * e[h])) /
                      1e3,
                        E[4 * h + 1] =
                            F.round(
                                1e3 *
                                (y * t[h] + v * s[h] + b * i[h] + _ * e[h])) /
                      1e3,
                        E[4 * h + 2] =
                            F.round(
                                1e3 *
                                (k * t[h] + A * s[h] + P * i[h] + S * e[h])) /
                      1e3,
                        E[4 * h + 3] =
                            F.round(
                                1e3 *
                                (C * t[h] + D * s[h] + x * i[h] + w * e[h])) /
                      1e3;
                return E
              },
          getPointInSegment:
              function(t, e, s, i, a, r) {
                var n = T(a, r), h = 1 - n;
                return [
                  F.round(
                      1e3 *
                      (h * h * h * t[0] +
                       (n * h * h + h * n * h + h * h * n) * s[0] +
                       (n * n * h + h * n * n + n * h * n) * i[0] +
                       n * n * n * e[0])) /
                      1e3,
                  F.round(
                      1e3 *
                      (h * h * h * t[1] +
                       (n * h * h + h * n * h + h * h * n) * s[1] +
                       (n * n * h + h * n * n + n * h * n) * i[1] +
                       n * n * n * e[1])) /
                      1e3
                ]
              },
          buildBezierData: t, pointOnLine2D: g,
          pointOnLine3D: function(t, e, s, i, a, r, n, h, o) {
            if (0 === s && 0 === r && 0 === o) return g(t, e, i, a, n, h);
            var l,
                p = F.sqrt(F.pow(i - t, 2) + F.pow(a - e, 2) + F.pow(r - s, 2)),
                f = F.sqrt(F.pow(n - t, 2) + F.pow(h - e, 2) + F.pow(o - s, 2)),
                d = F.sqrt(F.pow(n - i, 2) + F.pow(h - a, 2) + F.pow(o - r, 2));
            return -1e-4 < (l = f < p ? d < p ? p - f - d : d - f - p :
                                f < d ? d - f - p :
                                        f - p - d) &&
                l < 1e-4
          }
    }
  }();
  var L = function() {
    function d(t, e, s) {
      var i, a, r, n, h, o, l, p = t.length;
      for (a = 0; a < p; a += 1)
        if ('ks' in (i = t[a]) && !i.completed) {
          if (i.completed = !0, i.tt && (t[a - 1].td = i.tt), i.hasMask) {
            var f = i.masksProperties;
            for (n = f.length, r = 0; r < n; r += 1)
              if (f[r].pt.k.i)
                u(f[r].pt.k);
              else
                for (o = f[r].pt.k.length, h = 0; h < o; h += 1)
                  f[r].pt.k[h].s && u(f[r].pt.k[h].s[0]),
                      f[r].pt.k[h].e && u(f[r].pt.k[h].e[0])
          }
          0 === i.ty     ? (i.layers = m(i.refId, e), d(i.layers, e, s)) :
              4 === i.ty ? c(i.shapes) :
                           5 === i.ty &&
                  (0 !== (l = i).t.a.length || 'm' in l.t.p ||
                   (l.singleShape = !0))
        }
    }
    function m(t, e) {
      for (var s = 0, i = e.length; s < i;) {
        if (e[s].id === t)
          return e[s].layers.__used ? JSON.parse(JSON.stringify(e[s].layers)) :
                                      (e[s].layers.__used = !0, e[s].layers);
        s += 1
      }
      return null
    }
    function c(t) {
      var e, s, i;
      for (e = t.length - 1; 0 <= e; e -= 1)
        if ('sh' === t[e].ty)
          if (t[e].ks.k.i)
            u(t[e].ks.k);
          else
            for (i = t[e].ks.k.length, s = 0; s < i; s += 1)
              t[e].ks.k[s].s && u(t[e].ks.k[s].s[0]),
                  t[e].ks.k[s].e && u(t[e].ks.k[s].e[0]);
        else
          'gr' === t[e].ty && c(t[e].it)
    }
    function u(t) {
      var e, s = t.i.length;
      for (e = 0; e < s; e += 1)
        t.i[e][0] += t.v[e][0], t.i[e][1] += t.v[e][1], t.o[e][0] += t.v[e][0],
            t.o[e][1] += t.v[e][1]
    }
    function h(t, e) {
      var s = e ? e.split('.') : [100, 100, 100];
      return t[0] > s[0] ||
          !(s[0] > t[0]) &&
          (t[1] > s[1] ||
           !(s[1] > t[1]) && (t[2] > s[2] || !(s[2] > t[2]) && null))
    }
    var o, s = function() {
      var i = [4, 4, 14];
      function a(t) {
        var e, s, i, a = t.length;
        for (e = 0; e < a; e += 1)
          5 === t[e].ty && (s = t[e], i = s.t.d, s.t.d = {k: [{s: i, t: 0}]})
      }
      return function(t) {
        if (h(i, t.v) && (a(t.layers), t.assets)) {
          var e, s = t.assets.length;
          for (e = 0; e < s; e += 1) t.assets[e].layers && a(t.assets[e].layers)
        }
      }
    }(), i = (o = [4, 7, 99], function(t) {
           if (t.chars && !h(o, t.v)) {
             var e, s, i, a, r, n = t.chars.length;
             for (e = 0; e < n; e += 1)
               if (t.chars[e].data && t.chars[e].data.shapes)
                 for (i = (r = t.chars[e].data.shapes[0].it).length, s = 0;
                      s < i; s += 1)
                   (a = r[s].ks.k).__converted ||
                       (u(r[s].ks.k), a.__converted = !0)
           }
         }), a = function() {
      var i = [4, 1, 9];
      function r(t) {
        var e, s, i, a = t.length;
        for (e = 0; e < a; e += 1)
          if ('gr' === t[e].ty)
            r(t[e].it);
          else if ('fl' === t[e].ty || 'st' === t[e].ty)
            if (t[e].c.k && t[e].c.k[0].i)
              for (i = t[e].c.k.length, s = 0; s < i; s += 1)
                t[e].c.k[s].s &&
                    (t[e].c.k[s].s[0] /= 255, t[e].c.k[s].s[1] /= 255,
                     t[e].c.k[s].s[2] /= 255, t[e].c.k[s].s[3] /= 255),
                    t[e].c.k[s].e &&
                    (t[e].c.k[s].e[0] /= 255, t[e].c.k[s].e[1] /= 255,
                     t[e].c.k[s].e[2] /= 255, t[e].c.k[s].e[3] /= 255);
            else
              t[e].c.k[0] /= 255, t[e].c.k[1] /= 255, t[e].c.k[2] /= 255,
                  t[e].c.k[3] /= 255
      }
      function a(t) {
        var e, s = t.length;
        for (e = 0; e < s; e += 1) 4 === t[e].ty && r(t[e].shapes)
      }
      return function(t) {
        if (h(i, t.v) && (a(t.layers), t.assets)) {
          var e, s = t.assets.length;
          for (e = 0; e < s; e += 1) t.assets[e].layers && a(t.assets[e].layers)
        }
      }
    }(), r = function() {
      var i = [4, 4, 18];
      function l(t) {
        var e, s, i;
        for (e = t.length - 1; 0 <= e; e -= 1)
          if ('sh' === t[e].ty)
            if (t[e].ks.k.i)
              t[e].ks.k.c = t[e].closed;
            else
              for (i = t[e].ks.k.length, s = 0; s < i; s += 1)
                t[e].ks.k[s].s && (t[e].ks.k[s].s[0].c = t[e].closed),
                    t[e].ks.k[s].e && (t[e].ks.k[s].e[0].c = t[e].closed);
          else
            'gr' === t[e].ty && l(t[e].it)
      }
      function a(t) {
        var e, s, i, a, r, n, h = t.length;
        for (s = 0; s < h; s += 1) {
          if ((e = t[s]).hasMask) {
            var o = e.masksProperties;
            for (a = o.length, i = 0; i < a; i += 1)
              if (o[i].pt.k.i)
                o[i].pt.k.c = o[i].cl;
              else
                for (n = o[i].pt.k.length, r = 0; r < n; r += 1)
                  o[i].pt.k[r].s && (o[i].pt.k[r].s[0].c = o[i].cl),
                      o[i].pt.k[r].e && (o[i].pt.k[r].e[0].c = o[i].cl)
          }
          4 === e.ty && l(e.shapes)
        }
      }
      return function(t) {
        if (h(i, t.v) && (a(t.layers), t.assets)) {
          var e, s = t.assets.length;
          for (e = 0; e < s; e += 1) t.assets[e].layers && a(t.assets[e].layers)
        }
      }
    }();
    var t = {
      completeData: function(t, e) {
        t.__complete ||
            (a(t), s(t), i(t), r(t), d(t.layers, t.assets, e),
             t.__complete = !0)
      }
    };
    return t.checkColors = a, t.checkChars = i, t.checkShapes = r,
           t.completeLayers = d, t
  }();
  function q(t) {
    for (var e = t.fStyle ? t.fStyle.split(' ') : [], s = 'normal',
             i = 'normal', a = e.length, r = 0;
         r < a; r += 1)
      switch (e[r].toLowerCase()) {
        case 'italic':
          i = 'italic';
          break;
        case 'bold':
          s = '700';
          break;
        case 'black':
          s = '900';
          break;
        case 'medium':
          s = '500';
          break;
        case 'regular':
        case 'normal':
          s = '400';
          break;
        case 'light':
        case 'thin':
          s = '200'
      }
    return {
      style: i, weight: t.fWeight || s
    }
  }
  var V = function() {
    var r = {w: 0, size: 0, shapes: []}, t = [];
    function d(t, e) {
      var s = w('span');
      s.setAttribute('aria-hidden', !0), s.style.fontFamily = e;
      var i = w('span');
      i.innerText = 'giItT1WQy@!-/#', s.style.position = 'absolute',
      s.style.left = '-10000px', s.style.top = '-10000px',
      s.style.fontSize = '300px', s.style.fontVariant = 'normal',
      s.style.fontStyle = 'normal', s.style.fontWeight = 'normal',
      s.style.letterSpacing = '0', s.appendChild(i),
      document.body.appendChild(s);
      var a = i.offsetWidth;
      return i.style.fontFamily = function(t) {
        var e, s = t.split(','), i = s.length, a = [];
        for (e = 0; e < i; e += 1)
          'sans-serif' !== s[e] && 'monospace' !== s[e] && a.push(s[e]);
        return a.join(',')
      }(t) + ', ' + e, {
        node: i, w: a, parent: s
      }
    }
    function m(t, e) {
      var s = x('text');
      s.style.fontSize = '100px';
      var i = q(e);
      return s.setAttribute('font-family', e.fFamily),
             s.setAttribute('font-style', i.style),
             s.setAttribute('font-weight', i.weight),
             s.textContent = '1',
             e.fClass ? (s.style.fontFamily = 'inherit',
                         s.setAttribute('class', e.fClass)) :
                        s.style.fontFamily = e.fFamily,
             t.appendChild(s),
             w('canvas').getContext('2d').font =
                 e.fWeight + ' ' + e.fStyle + ' 100px ' + e.fFamily,
             s
    }
    t = t.concat([
      2304, 2305, 2306, 2307, 2362, 2363, 2364, 2364, 2366, 2367, 2368,
      2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379,
      2380, 2381, 2382, 2383, 2387, 2388, 2389, 2390, 2391, 2402, 2403
    ]);
    var e = function() {
      this.fonts = [], this.chars = null, this.typekitLoaded = 0,
      this.isLoaded = !1, this._warned = !1, this.initTime = Date.now(),
      this.setIsLoadedBinded = this.setIsLoaded.bind(this),
      this.checkLoadedFontsBinded = this.checkLoadedFonts.bind(this)
    };
    return e.getCombinedCharacterCodes =
               function() {
      return t
    },
           e.prototype = {
             addChars: function(t) {
               if (t) {
                 var e;
                 this.chars || (this.chars = []);
                 var s, i, a = t.length, r = this.chars.length;
                 for (e = 0; e < a; e += 1) {
                   for (s = 0, i = !1; s < r;)
                     this.chars[s].style === t[e].style &&
                         this.chars[s].fFamily === t[e].fFamily &&
                         this.chars[s].ch === t[e].ch && (i = !0),
                         s += 1;
                   i || (this.chars.push(t[e]), r += 1)
                 }
               }
             },
             addFonts: function(t, e) {
               if (t) {
                 if (this.chars)
                   return this.isLoaded = !0, void (this.fonts = t.list);
                 var s, i = t.list, a = i.length, r = a;
                 for (s = 0; s < a; s += 1) {
                   var n, h, o = !0;
                   if (i[s].loaded = !1,
                       i[s].monoCase = d(i[s].fFamily, 'monospace'),
                       i[s].sansCase = d(i[s].fFamily, 'sans-serif'),
                       i[s].fPath) {
                     if ('p' === i[s].fOrigin || 3 === i[s].origin) {
                       if (0 < (n = document.querySelectorAll(
                                    'style[f-forigin="p"][f-family="' +
                                    i[s].fFamily +
                                    '"], style[f-origin="3"][f-family="' +
                                    i[s].fFamily + '"]'))
                                       .length &&
                               (o = !1),
                           o) {
                         var l = w('style');
                         l.setAttribute('f-forigin', i[s].fOrigin),
                             l.setAttribute('f-origin', i[s].origin),
                             l.setAttribute('f-family', i[s].fFamily),
                             l.type = 'text/css',
                             l.innerText =
                                 '@font-face {font-family: ' + i[s].fFamily +
                             '; font-style: normal; src: url(\'' + i[s].fPath +
                             '\');}',
                             e.appendChild(l)
                       }
                     } else if ('g' === i[s].fOrigin || 1 === i[s].origin) {
                       for (n = document.querySelectorAll(
                                'link[f-forigin="g"], link[f-origin="1"]'),
                           h = 0;
                            h < n.length; h += 1)
                         -1 !== n[h].href.indexOf(i[s].fPath) && (o = !1);
                       if (o) {
                         var p = w('link');
                         p.setAttribute('f-forigin', i[s].fOrigin),
                             p.setAttribute('f-origin', i[s].origin),
                             p.type = 'text/css', p.rel = 'stylesheet',
                             p.href = i[s].fPath, document.body.appendChild(p)
                       }
                     } else if ('t' === i[s].fOrigin || 2 === i[s].origin) {
                       for (n = document.querySelectorAll(
                                'script[f-forigin="t"], script[f-origin="2"]'),
                           h = 0;
                            h < n.length; h += 1)
                         i[s].fPath === n[h].src && (o = !1);
                       if (o) {
                         var f = w('link');
                         f.setAttribute('f-forigin', i[s].fOrigin),
                             f.setAttribute('f-origin', i[s].origin),
                             f.setAttribute('rel', 'stylesheet'),
                             f.setAttribute('href', i[s].fPath),
                             e.appendChild(f)
                       }
                     }
                   } else
                     i[s].loaded = !0, r -= 1;
                   i[s].helper = m(e, i[s]), i[s].cache = {},
                   this.fonts.push(i[s])
                 }
                 0 === r ? this.isLoaded = !0 :
                           setTimeout(this.checkLoadedFonts.bind(this), 100)
               } else
                 this.isLoaded = !0
             },
             getCharData: function(t, e, s) {
               for (var i = 0, a = this.chars.length; i < a;) {
                 if (this.chars[i].ch === t && this.chars[i].style === e &&
                     this.chars[i].fFamily === s)
                   return this.chars[i];
                 i += 1
               }
               return ('string' == typeof t && 13 !== t.charCodeAt(0) || !t) &&
                          console && console.warn && !this._warned &&
                          (this._warned = !0,
                           console.warn(
                               'Missing character from exported characters list: ',
                               t, e, s)),
                      r
             },
             getFontByName: function(t) {
               for (var e = 0, s = this.fonts.length; e < s;) {
                 if (this.fonts[e].fName === t) return this.fonts[e];
                 e += 1
               }
               return this.fonts[0]
             },
             measureText: function(t, e, s) {
               var i = this.getFontByName(e), a = t.charCodeAt(0);
               if (!i.cache[a + 1]) {
                 var r = i.helper;
                 if (' ' === t) {
                   r.textContent = '|' + t + '|';
                   var n = r.getComputedTextLength();
                   r.textContent = '||';
                   var h = r.getComputedTextLength();
                   i.cache[a + 1] = (n - h) / 100
                 } else
                   r.textContent = t,
                   i.cache[a + 1] = r.getComputedTextLength() / 100
               }
               return i.cache[a + 1] * s
             },
             checkLoadedFonts: function() {
               var t, e, s, i = this.fonts.length, a = i;
               for (t = 0; t < i; t += 1)
                 this.fonts[t].loaded ?
                     a -= 1 :
                     'n' === this.fonts[t].fOrigin ||
                         0 === this.fonts[t].origin ?
                     this.fonts[t].loaded = !0 :
                     (e = this.fonts[t].monoCase.node,
                      s = this.fonts[t].monoCase.w,
                      e.offsetWidth !== s ?
                          (a -= 1, this.fonts[t].loaded = !0) :
                          (e = this.fonts[t].sansCase.node,
                           s = this.fonts[t].sansCase.w,
                           e.offsetWidth !== s &&
                               (a -= 1, this.fonts[t].loaded = !0)),
                      this.fonts[t].loaded &&
                          (this.fonts[t].sansCase.parent.parentNode.removeChild(
                               this.fonts[t].sansCase.parent),
                           this.fonts[t].monoCase.parent.parentNode.removeChild(
                               this.fonts[t].monoCase.parent)));
               0 !== a && Date.now() - this.initTime < 5e3 ?
                   setTimeout(this.checkLoadedFontsBinded, 20) :
                   setTimeout(this.setIsLoadedBinded, 10)
             },
             setIsLoaded: function() {
               this.isLoaded = !0
             }
           },
           e
  }(), R = function() {
    var f = s, a = Math.abs;
    function d(t, e) {
      var s, i = this.offsetTime;
      'multidimensional' === this.propType &&
          (s = j('float32', this.pv.length));
      for (var a, r, n, h, o, l, p, f, d = e.lastIndex, m = d,
                                       c = this.keyframes.length - 1, u = !0;
           u;) {
        if (a = this.keyframes[m], r = this.keyframes[m + 1],
            m === c - 1 && t >= r.t - i) {
          a.h && (a = r), d = 0;
          break
        }
        if (r.t - i > t) {
          d = m;
          break
        }
        m < c - 1 ? m += 1 : (d = 0, u = !1)
      }
      var g, y, v, b, _, k, A, P, S, C, D = r.t - i, x = a.t - i;
      if (a.to) {
        a.bezierData ||
            (a.bezierData = dt.buildBezierData(a.s, r.s || a.e, a.to, a.ti));
        var w = a.bezierData;
        if (D <= t || t < x) {
          var F = D <= t ? w.points.length - 1 : 0;
          for (h = w.points[F].point.length, n = 0; n < h; n += 1)
            s[n] = w.points[F].point[n]
        } else {
          a.__fnct ?
              f = a.__fnct :
              (f = W.getBezierEasing(a.o.x, a.o.y, a.i.x, a.i.y, a.n).get,
               a.__fnct = f),
              o = f((t - x) / (D - x));
          var T, E = w.segmentLength * o,
                 M = e.lastFrame < t && e._lastKeyframeIndex === m ?
              e._lastAddedLength :
              0;
          for (p = e.lastFrame < t && e._lastKeyframeIndex === m ?
                   e._lastPoint :
                   0,
              u = !0, l = w.points.length;
               u;) {
            if (M += w.points[p].partialLength,
                0 === E || 0 === o || p === w.points.length - 1) {
              for (h = w.points[p].point.length, n = 0; n < h; n += 1)
                s[n] = w.points[p].point[n];
              break
            }
            if (M <= E && E < M + w.points[p + 1].partialLength) {
              for (T = (E - M) / w.points[p + 1].partialLength,
                  h = w.points[p].point.length, n = 0;
                   n < h; n += 1)
                s[n] = w.points[p].point[n] +
                    (w.points[p + 1].point[n] - w.points[p].point[n]) * T;
              break
            }
            p < l - 1 ? p += 1 : u = !1
          }
          e._lastPoint = p, e._lastAddedLength = M - w.points[p].partialLength,
          e._lastKeyframeIndex = m
        }
      } else {
        var I, L, V, R, z;
        if (c = a.s.length, g = r.s || a.e, this.sh && 1 !== a.h)
          if (D <= t)
            s[0] = g[0], s[1] = g[1], s[2] = g[2];
          else if (t <= x)
            s[0] = a.s[0], s[1] = a.s[1], s[2] = a.s[2];
          else {
            var N = q(a.s), O = q(g);
            y = s,
            v =
                function(t, e, s) {
              var i, a, r, n, h, o = [], l = t[0], p = t[1], f = t[2], d = t[3],
                                 m = e[0], c = e[1], u = e[2], g = e[3];
              (a = l * m + p * c + f * u + d * g) < 0 &&
                  (a = -a, m = -m, c = -c, u = -u, g = -g);
              h = 1e-6 < 1 - a ?
                  (i = Math.acos(a), r = Math.sin(i),
                   n = Math.sin((1 - s) * i) / r, Math.sin(s * i) / r) :
                  (n = 1 - s, s);
              return o[0] = n * l + h * m, o[1] = n * p + h * c,
                     o[2] = n * f + h * u, o[3] = n * d + h * g, o
            }(N, O, (t - x) / (D - x)),
            b = v[0], _ = v[1], k = v[2], A = v[3],
            P = Math.atan2(2 * _ * A - 2 * b * k, 1 - 2 * _ * _ - 2 * k * k),
            S = Math.asin(2 * b * _ + 2 * k * A),
            C = Math.atan2(2 * b * A - 2 * _ * k, 1 - 2 * b * b - 2 * k * k),
            y[0] = P / B, y[1] = S / B, y[2] = C / B
          }
        else
          for (m = 0; m < c; m += 1)
            1 !== a.h &&
                (o = D <= t ?
                     1 :
                     t < x ?
                     0 :
                     (a.o.x.constructor === Array ?
                          (a.__fnct || (a.__fnct = []),
                           a.__fnct[m] ?
                               f = a.__fnct[m] :
                               (I = void 0 === a.o.x[m] ? a.o.x[0] : a.o.x[m],
                                L = void 0 === a.o.y[m] ? a.o.y[0] : a.o.y[m],
                                V = void 0 === a.i.x[m] ? a.i.x[0] : a.i.x[m],
                                R = void 0 === a.i.y[m] ? a.i.y[0] : a.i.y[m],
                                f = W.getBezierEasing(I, L, V, R).get,
                                a.__fnct[m] = f)) :
                          a.__fnct ?
                          f = a.__fnct :
                          (I = a.o.x, L = a.o.y, V = a.i.x, R = a.i.y,
                           f = W.getBezierEasing(I, L, V, R).get, a.__fnct = f),
                      f((t - x) / (D - x)))),
                g = r.s || a.e,
                z = 1 === a.h ? a.s[m] : a.s[m] + (g[m] - a.s[m]) * o,
                'multidimensional' === this.propType ? s[m] = z : s = z
      }
      return e.lastIndex = d, s
    }
    function q(t) {
      var e = t[0] * B, s = t[1] * B, i = t[2] * B, a = Math.cos(e / 2),
          r = Math.cos(s / 2), n = Math.cos(i / 2), h = Math.sin(e / 2),
          o = Math.sin(s / 2), l = Math.sin(i / 2);
      return [
        h * o * n + a * r * l, h * r * n + a * o * l, a * o * n - h * r * l,
        a * r * n - h * o * l
      ]
    }
    function m() {
      var t = this.comp.renderedFrame - this.offsetTime,
          e = this.keyframes[0].t - this.offsetTime,
          s = this.keyframes[this.keyframes.length - 1].t - this.offsetTime;
      if (!(t === this._caching.lastFrame ||
            this._caching.lastFrame !== f &&
                (this._caching.lastFrame >= s && s <= t ||
                 this._caching.lastFrame < e && t < e))) {
        this._caching.lastFrame >= t &&
            (this._caching._lastKeyframeIndex = -1,
             this._caching.lastIndex = 0);
        var i = this.interpolateValue(t, this._caching);
        this.pv = i
      }
      return this._caching.lastFrame = t, this.pv
    }
    function c(t) {
      var e;
      if ('unidimensional' === this.propType)
        e = t * this.mult, 1e-5 < a(this.v - e) && (this.v = e, this._mdf = !0);
      else
        for (var s = 0, i = this.v.length; s < i;)
          e = t[s] * this.mult,
          1e-5 < a(this.v[s] - e) && (this.v[s] = e, this._mdf = !0), s += 1
    }
    function u() {
      if (this.elem.globalData.frameId !== this.frameId &&
          this.effectsSequence.length)
        if (this.lock)
          this.setVValue(this.pv);
        else {
          var t;
          this.lock = !0, this._mdf = this._isFirstFrame;
          var e = this.effectsSequence.length,
              s = this.kf ? this.pv : this.data.k;
          for (t = 0; t < e; t += 1) s = this.effectsSequence[t](s);
          this.setVValue(s), this._isFirstFrame = !1, this.lock = !1,
                             this.frameId = this.elem.globalData.frameId
        }
    }
    function g(t) {
      this.effectsSequence.push(t), this.container.addDynamicProperty(this)
    }
    function n(t, e, s, i) {
      this.propType = 'unidimensional', this.mult = s || 1, this.data = e,
      this.v = s ? e.k * s : e.k, this.pv = e.k, this._mdf = !1, this.elem = t,
      this.container = i, this.comp = t.comp, this.k = !1, this.kf = !1,
      this.vel = 0, this.effectsSequence = [], this._isFirstFrame = !0,
      this.getValue = u, this.setVValue = c, this.addEffect = g
    }
    function h(t, e, s, i) {
      var a;
      this.propType = 'multidimensional', this.mult = s || 1, this.data = e,
      this._mdf = !1, this.elem = t, this.container = i, this.comp = t.comp,
      this.k = !1, this.kf = !1, this.frameId = -1;
      var r = e.k.length;
      for (this.v = j('float32', r), this.pv = j('float32', r),
          this.vel = j('float32', r), a = 0;
           a < r; a += 1)
        this.v[a] = e.k[a] * this.mult, this.pv[a] = e.k[a];
      this._isFirstFrame = !0, this.effectsSequence = [], this.getValue = u,
      this.setVValue = c, this.addEffect = g
    }
    function o(t, e, s, i) {
      this.propType = 'unidimensional', this.keyframes = e.k,
      this.offsetTime = t.data.st, this.frameId = -1,
      this._caching =
          {lastFrame: f, lastIndex: 0, value: 0, _lastKeyframeIndex: -1},
      this.k = !0, this.kf = !0, this.data = e, this.mult = s || 1,
      this.elem = t, this.container = i, this.comp = t.comp, this.v = f,
      this.pv = f, this._isFirstFrame = !0, this.getValue = u,
      this.setVValue = c, this.interpolateValue = d,
      this.effectsSequence = [m.bind(this)], this.addEffect = g
    }
    function l(t, e, s, i) {
      var a;
      this.propType = 'multidimensional';
      var r, n, h, o, l = e.k.length;
      for (a = 0; a < l - 1; a += 1)
        e.k[a].to && e.k[a].s && e.k[a + 1] && e.k[a + 1].s &&
            (r = e.k[a].s, n = e.k[a + 1].s, h = e.k[a].to, o = e.k[a].ti,
             (2 === r.length && (r[0] !== n[0] || r[1] !== n[1]) &&
                  dt.pointOnLine2D(
                      r[0], r[1], n[0], n[1], r[0] + h[0], r[1] + h[1]) &&
                  dt.pointOnLine2D(
                      r[0], r[1], n[0], n[1], n[0] + o[0], n[1] + o[1]) ||
              3 === r.length &&
                  (r[0] !== n[0] || r[1] !== n[1] || r[2] !== n[2]) &&
                  dt.pointOnLine3D(
                      r[0], r[1], r[2], n[0], n[1], n[2], r[0] + h[0],
                      r[1] + h[1], r[2] + h[2]) &&
                  dt.pointOnLine3D(
                      r[0], r[1], r[2], n[0], n[1], n[2], n[0] + o[0],
                      n[1] + o[1], n[2] + o[2])) &&
                 (e.k[a].to = null, e.k[a].ti = null),
             r[0] === n[0] && r[1] === n[1] && 0 === h[0] && 0 === h[1] &&
                 0 === o[0] && 0 === o[1] &&
                 (2 === r.length ||
                  r[2] === n[2] && 0 === h[2] && 0 === o[2]) &&
                 (e.k[a].to = null, e.k[a].ti = null));
      this.effectsSequence = [m.bind(this)], this.data = e,
      this.keyframes = e.k, this.offsetTime = t.data.st, this.k = !0,
      this.kf = !0, this._isFirstFrame = !0, this.mult = s || 1, this.elem = t,
      this.container = i, this.comp = t.comp, this.getValue = u,
      this.setVValue = c, this.interpolateValue = d, this.frameId = -1;
      var p = e.k[0].s.length;
      for (this.v = j('float32', p), this.pv = j('float32', p), a = 0; a < p;
           a += 1)
        this.v[a] = f, this.pv[a] = f;
      this._caching = {lastFrame: f, lastIndex: 0, value: j('float32', p)},
      this.addEffect = g
    }
    return {
      getProp: function(t, e, s, i, a) {
        var r;
        if (e.k.length)
          if ('number' == typeof e.k[0])
            r = new h(t, e, i, a);
          else
            switch (s) {
              case 0:
                r = new o(t, e, i, a);
                break;
              case 1:
                r = new l(t, e, i, a)
            }
        else
          r = new n(t, e, i, a);
        return r.effectsSequence.length && a.addDynamicProperty(r), r
      }
    }
  }(), z = function() {
    var n = [0, 0];
    function i(t, e, s) {
      if (this.elem = t, this.frameId = -1, this.propType = 'transform',
          this.data = e, this.v = new I, this.pre = new I,
          this.appliedTransformations = 0,
          this.initDynamicPropertyContainer(s || t),
          e.p && e.p.s ?
              (this.px = R.getProp(t, e.p.x, 0, 0, this),
               this.py = R.getProp(t, e.p.y, 0, 0, this),
               e.p.z && (this.pz = R.getProp(t, e.p.z, 0, 0, this))) :
              this.p = R.getProp(t, e.p || {k: [0, 0, 0]}, 1, 0, this),
          e.rx) {
        if (this.rx = R.getProp(t, e.rx, 0, B, this),
            this.ry = R.getProp(t, e.ry, 0, B, this),
            this.rz = R.getProp(t, e.rz, 0, B, this), e.or.k[0].ti) {
          var i, a = e.or.k.length;
          for (i = 0; i < a; i += 1) e.or.k[i].to = null, e.or.k[i].ti = null
        }
        this.or = R.getProp(t, e.or, 1, B, this), this.or.sh = !0
      } else
        this.r = R.getProp(t, e.r || {k: 0}, 0, B, this);
      e.sk &&
          (this.sk = R.getProp(t, e.sk, 0, B, this),
           this.sa = R.getProp(t, e.sa, 0, B, this)),
          this.a = R.getProp(t, e.a || {k: [0, 0, 0]}, 1, 0, this),
          this.s = R.getProp(t, e.s || {k: [100, 100, 100]}, 1, .01, this),
          e.o ? this.o = R.getProp(t, e.o, 0, .01, t) :
                this.o = {_mdf: !1, v: 1},
          this._isDirty = !0, this.dynamicProperties.length || this.getValue(!0)
    }
    return i.prototype = {
      applyToMatrix: function(t) {
        var e = this._mdf;
        this.iterateDynamicProperties(),
            this._mdf = this._mdf || e,
            this.a && t.translate(-this.a.v[0], -this.a.v[1], this.a.v[2]),
            this.s && t.scale(this.s.v[0], this.s.v[1], this.s.v[2]),
            this.sk && t.skewFromAxis(-this.sk.v, this.sa.v),
            this.r ? t.rotate(-this.r.v) :
                     t.rotateZ(-this.rz.v)
                         .rotateY(this.ry.v)
                         .rotateX(this.rx.v)
                         .rotateZ(-this.or.v[2])
                         .rotateY(this.or.v[1])
                         .rotateX(this.or.v[0]),
            this.data.p.s ? this.data.p.z ?
                            t.translate(this.px.v, this.py.v, -this.pz.v) :
                            t.translate(this.px.v, this.py.v, 0) :
                            t.translate(this.p.v[0], this.p.v[1], -this.p.v[2])
      },
      getValue: function(t) {
        if (this.elem.globalData.frameId !== this.frameId) {
          if (this._isDirty && (this.precalculateMatrix(), this._isDirty = !1),
              this.iterateDynamicProperties(), this._mdf || t) {
            var e;
            if (this.v.cloneFromProps(this.pre.props),
                this.appliedTransformations < 1 &&
                    this.v.translate(-this.a.v[0], -this.a.v[1], this.a.v[2]),
                this.appliedTransformations < 2 &&
                    this.v.scale(this.s.v[0], this.s.v[1], this.s.v[2]),
                this.sk && this.appliedTransformations < 3 &&
                    this.v.skewFromAxis(-this.sk.v, this.sa.v),
                this.r && this.appliedTransformations < 4 ?
                    this.v.rotate(-this.r.v) :
                    !this.r && this.appliedTransformations < 4 &&
                        this.v.rotateZ(-this.rz.v)
                            .rotateY(this.ry.v)
                            .rotateX(this.rx.v)
                            .rotateZ(-this.or.v[2])
                            .rotateY(this.or.v[1])
                            .rotateX(this.or.v[0]),
                this.autoOriented) {
              var s, i;
              if (e = this.elem.globalData.frameRate,
                  this.p && this.p.keyframes && this.p.getValueAtTime)
                i = this.p._caching.lastFrame + this.p.offsetTime <=
                        this.p.keyframes[0].t ?
                    (s = this.p.getValueAtTime(
                         (this.p.keyframes[0].t + .01) / e, 0),
                     this.p.getValueAtTime(this.p.keyframes[0].t / e, 0)) :
                    this.p._caching.lastFrame + this.p.offsetTime >=
                        this.p.keyframes[this.p.keyframes.length - 1].t ?
                    (s = this.p.getValueAtTime(
                         this.p.keyframes[this.p.keyframes.length - 1].t / e,
                         0),
                     this.p.getValueAtTime(
                         (this.p.keyframes[this.p.keyframes.length - 1].t -
                          .05) /
                             e,
                         0)) :
                    (s = this.p.pv,
                     this.p.getValueAtTime(
                         (this.p._caching.lastFrame + this.p.offsetTime - .01) /
                             e,
                         this.p.offsetTime));
              else if (
                  this.px && this.px.keyframes && this.py.keyframes &&
                  this.px.getValueAtTime && this.py.getValueAtTime) {
                s = [], i = [];
                var a = this.px, r = this.py;
                a._caching.lastFrame + a.offsetTime <= a.keyframes[0].t ?
                    (s[0] = a.getValueAtTime((a.keyframes[0].t + .01) / e, 0),
                     s[1] = r.getValueAtTime((r.keyframes[0].t + .01) / e, 0),
                     i[0] = a.getValueAtTime(a.keyframes[0].t / e, 0),
                     i[1] = r.getValueAtTime(r.keyframes[0].t / e, 0)) :
                    a._caching.lastFrame + a.offsetTime >=
                        a.keyframes[a.keyframes.length - 1].t ?
                    (s[0] = a.getValueAtTime(
                         a.keyframes[a.keyframes.length - 1].t / e, 0),
                     s[1] = r.getValueAtTime(
                         r.keyframes[r.keyframes.length - 1].t / e, 0),
                     i[0] = a.getValueAtTime(
                         (a.keyframes[a.keyframes.length - 1].t - .01) / e, 0),
                     i[1] = r.getValueAtTime(
                         (r.keyframes[r.keyframes.length - 1].t - .01) / e,
                         0)) :
                    (s = [a.pv, r.pv],
                     i[0] = a.getValueAtTime(
                         (a._caching.lastFrame + a.offsetTime - .01) / e,
                         a.offsetTime),
                     i[1] = r.getValueAtTime(
                         (r._caching.lastFrame + r.offsetTime - .01) / e,
                         r.offsetTime))
              } else
                s = i = n;
              this.v.rotate(-Math.atan2(s[1] - i[1], s[0] - i[0]))
            }
            this.data.p && this.data.p.s ?
                this.data.p.z ?
                this.v.translate(this.px.v, this.py.v, -this.pz.v) :
                this.v.translate(this.px.v, this.py.v, 0) :
                this.v.translate(this.p.v[0], this.p.v[1], -this.p.v[2])
          }
          this.frameId = this.elem.globalData.frameId
        }
      },
      precalculateMatrix: function() {
        if (!this.a.k &&
            (this.pre.translate(-this.a.v[0], -this.a.v[1], this.a.v[2]),
             this.appliedTransformations = 1, !this.s.effectsSequence.length)) {
          if (this.pre.scale(this.s.v[0], this.s.v[1], this.s.v[2]),
              this.appliedTransformations = 2, this.sk) {
            if (this.sk.effectsSequence.length ||
                this.sa.effectsSequence.length)
              return;
            this.pre.skewFromAxis(-this.sk.v, this.sa.v),
                this.appliedTransformations = 3
          }
          this.r ? this.r.effectsSequence.length ||
                  (this.pre.rotate(-this.r.v),
                   this.appliedTransformations = 4) :
                   this.rz.effectsSequence.length ||
                  this.ry.effectsSequence.length ||
                  this.rx.effectsSequence.length ||
                  this.or.effectsSequence.length ||
                  (this.pre.rotateZ(-this.rz.v)
                       .rotateY(this.ry.v)
                       .rotateX(this.rx.v)
                       .rotateZ(-this.or.v[2])
                       .rotateY(this.or.v[1])
                       .rotateX(this.or.v[0]),
                   this.appliedTransformations = 4)
        }
      },
      autoOrient: function() {}
    },
           M([F], i),
           i.prototype.addDynamicProperty =
               function(t) {
             this._addDynamicProperty(t), this.elem.addDynamicProperty(t),
                 this._isDirty = !0
           },
           i.prototype._addDynamicProperty = F.prototype.addDynamicProperty, {
      getTransformProperty: function(t, e, s) {
        return new i(t, e, s)
      }
    }
  }();
  function N() {
    this.c = !1, this._length = 0, this._maxLength = 8,
    this.v = D(this._maxLength), this.o = D(this._maxLength),
    this.i = D(this._maxLength)
  }
  N.prototype.setPathData = function(t, e) {
    this.c = t, this.setLength(e);
    for (var s = 0; s < e;)
      this.v[s] = Ct.newElement(), this.o[s] = Ct.newElement(),
      this.i[s] = Ct.newElement(), s += 1
  }, N.prototype.setLength = function(t) {
    for (; this._maxLength < t;) this.doubleArrayLength();
    this._length = t
  }, N.prototype.doubleArrayLength = function() {
    this.v = this.v.concat(D(this._maxLength)),
    this.i = this.i.concat(D(this._maxLength)),
    this.o = this.o.concat(D(this._maxLength)), this._maxLength *= 2
  }, N.prototype.setXYAt = function(t, e, s, i, a) {
    var r;
    switch (this._length = Math.max(this._length, i + 1),
            this._length >= this._maxLength && this.doubleArrayLength(), s) {
      case 'v':
        r = this.v;
        break;
      case 'i':
        r = this.i;
        break;
      case 'o':
        r = this.o;
        break;
      default:
        r = []
    }
    (!r[i] || r[i] && !a) && (r[i] = Ct.newElement()), r[i][0] = t, r[i][1] = e
  }, N.prototype.setTripleAt = function(t, e, s, i, a, r, n, h) {
    this.setXYAt(t, e, 'v', n, h), this.setXYAt(s, i, 'o', n, h),
        this.setXYAt(a, r, 'i', n, h)
  }, N.prototype.reverse = function() {
    var t = new N;
    t.setPathData(this.c, this._length);
    var e = this.v, s = this.o, i = this.i, a = 0;
    this.c &&
        (t.setTripleAt(
             e[0][0], e[0][1], i[0][0], i[0][1], s[0][0], s[0][1], 0, !1),
         a = 1);
    var r, n = this._length - 1, h = this._length;
    for (r = a; r < h; r += 1)
      t.setTripleAt(
          e[n][0], e[n][1], i[n][0], i[n][1], s[n][0], s[n][1], r, !1),
          n -= 1;
    return t
  };
  var O, X,
      H =
          function() {
        var a = -999999;
        function t(t, e, s) {
          var i, a, r, n, h, o, l, p, f, d = s.lastIndex, m = this.keyframes;
          if (t < m[0].t - this.offsetTime)
            i = m[0].s[0], r = !0, d = 0;
          else if (t >= m[m.length - 1].t - this.offsetTime)
            i = m[m.length - 1].s ? m[m.length - 1].s[0] : m[m.length - 2].e[0],
            r = !0;
          else {
            for (var c, u, g = d, y = m.length - 1, v = !0;
                 v && (c = m[g], !((u = m[g + 1]).t - this.offsetTime > t));)
              g < y - 1 ? g += 1 : v = !1;
            if (d = g, !(r = 1 === c.h)) {
              if (t >= u.t - this.offsetTime)
                p = 1;
              else if (t < c.t - this.offsetTime)
                p = 0;
              else {
                var b;
                c.__fnct ?
                    b = c.__fnct :
                    (b = W.getBezierEasing(c.o.x, c.o.y, c.i.x, c.i.y).get,
                     c.__fnct = b),
                    p =
                        b((t - (c.t - this.offsetTime)) /
                          (u.t - this.offsetTime - (c.t - this.offsetTime)))
              }
              a = u.s ? u.s[0] : c.e[0]
            }
            i = c.s[0]
          }
          for (o = e._length, l = i.i[0].length, s.lastIndex = d, n = 0; n < o;
               n += 1)
            for (h = 0; h < l; h += 1)
              f = r ? i.i[n][h] : i.i[n][h] + (a.i[n][h] - i.i[n][h]) * p,
              e.i[n][h] = f,
              f = r ? i.o[n][h] : i.o[n][h] + (a.o[n][h] - i.o[n][h]) * p,
              e.o[n][h] = f,
              f = r ? i.v[n][h] : i.v[n][h] + (a.v[n][h] - i.v[n][h]) * p,
              e.v[n][h] = f
        }
        function r() {
          this.paths = this.localShapeCollection
        }
        function e(t) {
          (function(t, e) {
            if (t._length !== e._length || t.c !== e.c) return !1;
            var s, i = t._length;
            for (s = 0; s < i; s += 1)
              if (t.v[s][0] !== e.v[s][0] || t.v[s][1] !== e.v[s][1] ||
                  t.o[s][0] !== e.o[s][0] || t.o[s][1] !== e.o[s][1] ||
                  t.i[s][0] !== e.i[s][0] || t.i[s][1] !== e.i[s][1])
                return !1;
            return !0
          })(this.v, t) ||
              (this.v = Dt.clone(t), this.localShapeCollection.releaseShapes(),
               this.localShapeCollection.addShape(this.v), this._mdf = !0,
               this.paths = this.localShapeCollection)
        }
        function s() {
          if (this.elem.globalData.frameId !== this.frameId)
            if (this.effectsSequence.length)
              if (this.lock)
                this.setVValue(this.pv);
              else {
                var t, e;
                this.lock = !0, this._mdf = !1,
                t = this.kf      ? this.pv :
                    this.data.ks ? this.data.ks.k :
                                   this.data.pt.k;
                var s = this.effectsSequence.length;
                for (e = 0; e < s; e += 1) t = this.effectsSequence[e](t);
                this.setVValue(t), this.lock = !1,
                                   this.frameId = this.elem.globalData.frameId
              }
            else
              this._mdf = !1
        }
        function n(t, e, s) {
          this.propType = 'shape', this.comp = t.comp, this.container = t,
          this.elem = t, this.data = e, this.k = !1, this.kf = !1,
          this._mdf = !1;
          var i = 3 === s ? e.pt.k : e.ks.k;
          this.v = Dt.clone(i), this.pv = Dt.clone(this.v),
          this.localShapeCollection = xt.newShapeCollection(),
          this.paths = this.localShapeCollection, this.paths.addShape(this.v),
          this.reset = r, this.effectsSequence = []
        }
        function i(t) {
          this.effectsSequence.push(t), this.container.addDynamicProperty(this)
        }
        function h(t, e, s) {
          this.propType = 'shape', this.comp = t.comp, this.elem = t,
          this.container = t, this.offsetTime = t.data.st,
          this.keyframes = 3 === s ? e.pt.k : e.ks.k, this.k = !0, this.kf = !0;
          var i = this.keyframes[0].s[0].i.length;
          this.v = Dt.newElement(),
          this.v.setPathData(this.keyframes[0].s[0].c, i),
          this.pv = Dt.clone(this.v),
          this.localShapeCollection = xt.newShapeCollection(),
          this.paths = this.localShapeCollection, this.paths.addShape(this.v),
          this.lastFrame = a, this.reset = r,
          this._caching = {lastFrame: a, lastIndex: 0},
          this.effectsSequence = [function() {
            var t = this.comp.renderedFrame - this.offsetTime,
                e = this.keyframes[0].t - this.offsetTime,
                s = this.keyframes[this.keyframes.length - 1].t -
                this.offsetTime,
                i = this._caching.lastFrame;
            return i !== a && (i < e && t < e || s < i && s < t) ||
                       (this._caching.lastIndex =
                            i < t ? this._caching.lastIndex : 0,
                        this.interpolateShape(t, this.pv, this._caching)),
                   this._caching.lastFrame = t, this.pv
          }.bind(this)]
        }
        n.prototype.interpolateShape = t, n.prototype.getValue = s,
        n.prototype.setVValue = e, n.prototype.addEffect = i,
        h.prototype.getValue = s, h.prototype.interpolateShape = t,
        h.prototype.setVValue = e, h.prototype.addEffect = i;
        var o = function() {
          var n = v;
          function t(t, e) {
            this.v = Dt.newElement(), this.v.setPathData(!0, 4),
            this.localShapeCollection = xt.newShapeCollection(),
            this.paths = this.localShapeCollection,
            this.localShapeCollection.addShape(this.v), this.d = e.d,
            this.elem = t, this.comp = t.comp, this.frameId = -1,
            this.initDynamicPropertyContainer(t),
            this.p = R.getProp(t, e.p, 1, 0, this),
            this.s = R.getProp(t, e.s, 1, 0, this),
            this.dynamicProperties.length ?
                this.k = !0 :
                (this.k = !1, this.convertEllToPath())
          }
          return t.prototype = {
            reset: r,
            getValue: function() {
              this.elem.globalData.frameId !== this.frameId &&
                  (this.frameId = this.elem.globalData.frameId,
                   this.iterateDynamicProperties(),
                   this._mdf && this.convertEllToPath())
            },
            convertEllToPath: function() {
              var t = this.p.v[0], e = this.p.v[1], s = this.s.v[0] / 2,
                  i = this.s.v[1] / 2, a = 3 !== this.d, r = this.v;
              r.v[0][0] = t, r.v[0][1] = e - i, r.v[1][0] = a ? t + s : t - s,
              r.v[1][1] = e, r.v[2][0] = t, r.v[2][1] = e + i,
              r.v[3][0] = a ? t - s : t + s, r.v[3][1] = e,
              r.i[0][0] = a ? t - s * n : t + s * n, r.i[0][1] = e - i,
              r.i[1][0] = a ? t + s : t - s, r.i[1][1] = e - i * n,
              r.i[2][0] = a ? t + s * n : t - s * n, r.i[2][1] = e + i,
              r.i[3][0] = a ? t - s : t + s, r.i[3][1] = e + i * n,
              r.o[0][0] = a ? t + s * n : t - s * n, r.o[0][1] = e - i,
              r.o[1][0] = a ? t + s : t - s, r.o[1][1] = e + i * n,
              r.o[2][0] = a ? t - s * n : t + s * n, r.o[2][1] = e + i,
              r.o[3][0] = a ? t - s : t + s, r.o[3][1] = e - i * n
            }
          },
                 M([F], t), t
        }(), l = function() {
          function t(t, e) {
            this.v = Dt.newElement(), this.v.setPathData(!0, 0), this.elem = t,
            this.comp = t.comp, this.data = e, this.frameId = -1, this.d = e.d,
            this.initDynamicPropertyContainer(t),
            1 === e.sy ? (this.ir = R.getProp(t, e.ir, 0, 0, this),
                          this.is = R.getProp(t, e.is, 0, .01, this),
                          this.convertToPath = this.convertStarToPath) :
                         this.convertToPath = this.convertPolygonToPath,
            this.pt = R.getProp(t, e.pt, 0, 0, this),
            this.p = R.getProp(t, e.p, 1, 0, this),
            this.r = R.getProp(t, e.r, 0, B, this),
            this.or = R.getProp(t, e.or, 0, 0, this),
            this.os = R.getProp(t, e.os, 0, .01, this),
            this.localShapeCollection = xt.newShapeCollection(),
            this.localShapeCollection.addShape(this.v),
            this.paths = this.localShapeCollection,
            this.dynamicProperties.length ? this.k = !0 :
                                            (this.k = !1, this.convertToPath())
          }
          return t.prototype = {
            reset: r,
            getValue: function() {
              this.elem.globalData.frameId !== this.frameId &&
                  (this.frameId = this.elem.globalData.frameId,
                   this.iterateDynamicProperties(),
                   this._mdf && this.convertToPath())
            },
            convertStarToPath: function() {
              var t, e, s, i,
                  a = 2 * Math.floor(this.pt.v), r = 2 * Math.PI / a, n = !0,
                  h = this.or.v, o = this.ir.v, l = this.os.v, p = this.is.v,
                  f = 2 * Math.PI * h / (2 * a), d = 2 * Math.PI * o / (2 * a),
                  m = -Math.PI / 2;
              m += this.r.v;
              var c = 3 === this.data.d ? -1 : 1;
              for (t = this.v._length = 0; t < a; t += 1) {
                s = n ? l : p, i = n ? f : d;
                var u = (e = n ? h : o) * Math.cos(m), g = e * Math.sin(m),
                    y = 0 === u && 0 === g ? 0 : g / Math.sqrt(u * u + g * g),
                    v = 0 === u && 0 === g ? 0 : -u / Math.sqrt(u * u + g * g);
                u += +this.p.v[0], g += +this.p.v[1],
                    this.v.setTripleAt(
                        u, g, u - y * i * s * c, g - v * i * s * c,
                        u + y * i * s * c, g + v * i * s * c, t, !0),
                    n = !n, m += r * c
              }
            },
            convertPolygonToPath: function() {
              var t, e = Math.floor(this.pt.v), s = 2 * Math.PI / e,
                     i = this.or.v, a = this.os.v,
                     r = 2 * Math.PI * i / (4 * e), n = .5 * -Math.PI,
                     h = 3 === this.data.d ? -1 : 1;
              for (n += this.r.v, t = this.v._length = 0; t < e; t += 1) {
                var o = i * Math.cos(n), l = i * Math.sin(n),
                    p = 0 === o && 0 === l ? 0 : l / Math.sqrt(o * o + l * l),
                    f = 0 === o && 0 === l ? 0 : -o / Math.sqrt(o * o + l * l);
                o += +this.p.v[0], l += +this.p.v[1],
                    this.v.setTripleAt(
                        o, l, o - p * r * a * h, l - f * r * a * h,
                        o + p * r * a * h, l + f * r * a * h, t, !0),
                    n += s * h
              }
              this.paths.length = 0, this.paths[0] = this.v
            }
          },
                 M([F], t), t
        }(), p = function() {
          function t(t, e) {
            this.v = Dt.newElement(), this.v.c = !0,
            this.localShapeCollection = xt.newShapeCollection(),
            this.localShapeCollection.addShape(this.v),
            this.paths = this.localShapeCollection, this.elem = t,
            this.comp = t.comp, this.frameId = -1, this.d = e.d,
            this.initDynamicPropertyContainer(t),
            this.p = R.getProp(t, e.p, 1, 0, this),
            this.s = R.getProp(t, e.s, 1, 0, this),
            this.r = R.getProp(t, e.r, 0, 0, this),
            this.dynamicProperties.length ?
                this.k = !0 :
                (this.k = !1, this.convertRectToPath())
          }
          return t.prototype = {
            convertRectToPath: function() {
              var t = this.p.v[0], e = this.p.v[1], s = this.s.v[0] / 2,
                  i = this.s.v[1] / 2, a = d(s, i, this.r.v), r = a * (1 - v);
              this.v._length = 0,
              2 === this.d || 1 === this.d ?
                  (this.v.setTripleAt(
                       t + s, e - i + a, t + s, e - i + a, t + s, e - i + r, 0,
                       !0),
                   this.v.setTripleAt(
                       t + s, e + i - a, t + s, e + i - r, t + s, e + i - a, 1,
                       !0),
                   0 !== a ?
                       (this.v.setTripleAt(
                            t + s - a, e + i, t + s - a, e + i, t + s - r,
                            e + i, 2, !0),
                        this.v.setTripleAt(
                            t - s + a, e + i, t - s + r, e + i, t - s + a,
                            e + i, 3, !0),
                        this.v.setTripleAt(
                            t - s, e + i - a, t - s, e + i - a, t - s,
                            e + i - r, 4, !0),
                        this.v.setTripleAt(
                            t - s, e - i + a, t - s, e - i + r, t - s,
                            e - i + a, 5, !0),
                        this.v.setTripleAt(
                            t - s + a, e - i, t - s + a, e - i, t - s + r,
                            e - i, 6, !0),
                        this.v.setTripleAt(
                            t + s - a, e - i, t + s - r, e - i, t + s - a,
                            e - i, 7, !0)) :
                       (this.v.setTripleAt(
                            t - s, e + i, t - s + r, e + i, t - s, e + i, 2),
                        this.v.setTripleAt(
                            t - s, e - i, t - s, e - i + r, t - s, e - i, 3))) :
                  (this.v.setTripleAt(
                       t + s, e - i + a, t + s, e - i + r, t + s, e - i + a, 0,
                       !0),
                   0 !== a ? (this.v.setTripleAt(
                                  t + s - a, e - i, t + s - a, e - i, t + s - r,
                                  e - i, 1, !0),
                              this.v.setTripleAt(
                                  t - s + a, e - i, t - s + r, e - i, t - s + a,
                                  e - i, 2, !0),
                              this.v.setTripleAt(
                                  t - s, e - i + a, t - s, e - i + a, t - s,
                                  e - i + r, 3, !0),
                              this.v.setTripleAt(
                                  t - s, e + i - a, t - s, e + i - r, t - s,
                                  e + i - a, 4, !0),
                              this.v.setTripleAt(
                                  t - s + a, e + i, t - s + a, e + i, t - s + r,
                                  e + i, 5, !0),
                              this.v.setTripleAt(
                                  t + s - a, e + i, t + s - r, e + i, t + s - a,
                                  e + i, 6, !0),
                              this.v.setTripleAt(
                                  t + s, e + i - a, t + s, e + i - a, t + s,
                                  e + i - r, 7, !0)) :
                             (this.v.setTripleAt(
                                  t - s, e - i, t - s + r, e - i, t - s, e - i,
                                  1, !0),
                              this.v.setTripleAt(
                                  t - s, e + i, t - s, e + i - r, t - s, e + i,
                                  2, !0),
                              this.v.setTripleAt(
                                  t + s, e + i, t + s - r, e + i, t + s, e + i,
                                  3, !0)))
            },
            getValue: function() {
              this.elem.globalData.frameId !== this.frameId &&
                  (this.frameId = this.elem.globalData.frameId,
                   this.iterateDynamicProperties(),
                   this._mdf && this.convertRectToPath())
            },
            reset: r
          },
                 M([F], t), t
        }();
        var f = {
          getShapeProp: function(t, e, s) {
            var i;
            return 3 === s || 4 === s ? i = (3 === s ? e.pt : e.ks).k.length ?
                                        new h(t, e, s) :
                                        new n(t, e, s) :
                       5 === s        ? i = new p(t, e) :
                       6 === s        ? i = new o(t, e) :
                                        7 === s && (i = new l(t, e)),
                                        i.k && t.addDynamicProperty(i), i
          },
          getConstructorFunction: function() {
            return n
          },
          getKeyframedConstructorFunction: function() {
            return h
          }
        };
        return f
      }(),
      Y =
          (X = {},
           (O = {}).registerModifier =
               function(t, e) {
                 X[t] || (X[t] = e)
               },
           O.getModifier =
               function(t, e, s) {
                 return new X[t](e, s)
               },
           O);
  function G() {}
  function K() {}
  function J() {}
  function U() {}
  function Z() {}
  function Q() {
    this._length = 0, this._maxLength = 4, this.shapes = D(this._maxLength)
  }
  function $(t, e, s, i) {
    var a;
    this.elem = t, this.frameId = -1, this.dataProps = D(e.length),
    this.renderer = s, this.k = !1, this.dashStr = '',
    this.dashArray = j('float32', e.length ? e.length - 1 : 0),
    this.dashoffset = j('float32', 1), this.initDynamicPropertyContainer(i);
    var r, n = e.length || 0;
    for (a = 0; a < n; a += 1)
      r = R.getProp(t, e[a].v, 0, 0, this), this.k = r.k || this.k,
      this.dataProps[a] = {n: e[a].n, p: r};
    this.k || this.getValue(!0), this._isAnimated = this.k
  }
  function tt(t, e, s) {
    this.data = e, this.c = j('uint8c', 4 * e.p);
    var i = e.k.k[0].s ? e.k.k[0].s.length - 4 * e.p : e.k.k.length - 4 * e.p;
    this.o = j('float32', i), this._cmdf = !1, this._omdf = !1,
    this._collapsable = this.checkCollapsable(), this._hasOpacity = i,
    this.initDynamicPropertyContainer(s),
    this.prop = R.getProp(t, e.k, 1, null, this), this.k = this.prop.k,
    this.getValue(!0)
  }
  G.prototype.initModifierProperties = function() {},
  G.prototype.addShapeToModifier = function() {},
  G.prototype.addShape =
      function(t) {
    if (!this.closed) {
      t.sh.container.addDynamicProperty(t.sh);
      var e = {
        shape: t.sh,
        data: t,
        localShapeCollection: xt.newShapeCollection()
      };
      this.shapes.push(e), this.addShapeToModifier(e),
          this._isAnimated && t.setAsAnimated()
    }
  },
  G.prototype.init =
      function(t, e) {
    this.shapes = [], this.elem = t, this.initDynamicPropertyContainer(t),
    this.initModifierProperties(t, e), this.frameId = s, this.closed = !1,
    this.k = !1, this.dynamicProperties.length ? this.k = !0 : this.getValue(!0)
  },
  G.prototype.processKeys =
      function() {
    this.elem.globalData.frameId !== this.frameId &&
        (this.frameId = this.elem.globalData.frameId,
         this.iterateDynamicProperties())
  },
  M([F], G), M([G], K),
  K.prototype.initModifierProperties =
      function(t, e) {
    this.s = R.getProp(t, e.s, 0, .01, this),
    this.e = R.getProp(t, e.e, 0, .01, this),
    this.o = R.getProp(t, e.o, 0, 0, this), this.sValue = 0, this.eValue = 0,
    this.getValue = this.processKeys, this.m = e.m,
    this._isAnimated = !!this.s.effectsSequence.length ||
        !!this.e.effectsSequence.length || !!this.o.effectsSequence.length
  },
  K.prototype.addShapeToModifier =
      function(t) {
    t.pathsData = []
  },
  K.prototype.calculateShapeEdges =
      function(t, e, s, i, a) {
    var r = [];
    e <= 1     ? r.push({s: t, e: e}) :
        1 <= t ? r.push({s: t - 1, e: e - 1}) :
                 (r.push({s: t, e: 1}), r.push({s: 0, e: e - 1}));
    var n, h, o = [], l = r.length;
    for (n = 0; n < l; n += 1) {
      var p, f;
      if (!((h = r[n]).e * a < i || h.s * a > i + s))
        p = h.s * a <= i ? 0 : (h.s * a - i) / s,
        f = h.e * a >= i + s ? 1 : (h.e * a - i) / s, o.push([p, f])
    }
    return o.length || o.push([0, 0]), o
  },
  K.prototype.releasePathsData =
      function(t) {
    var e, s = t.length;
    for (e = 0; e < s; e += 1) wt.release(t[e]);
    return t.length = 0, t
  },
  K.prototype.processShapes =
      function(t) {
    var e, s, i, a;
    if (this._mdf || t) {
      var r = this.o.v % 360 / 360;
      if (r < 0 && (r += 1),
          e = 1 < this.s.v ? 1 + r :
              this.s.v < 0 ? 0 + r :
                             this.s.v + r,
          (s = 1 < this.e.v ? 1 + r :
               this.e.v < 0 ? 0 + r :
                              this.e.v + r) < e) {
        var n = e;
        e = s, s = n
      }
      e = 1e-4 * Math.round(1e4 * e), s = 1e-4 * Math.round(1e4 * s),
      this.sValue = e, this.eValue = s
    } else
      e = this.sValue, s = this.eValue;
    var h, o, l, p, f, d = this.shapes.length, m = 0;
    if (s === e)
      for (a = 0; a < d; a += 1)
        this.shapes[a].localShapeCollection.releaseShapes(),
            this.shapes[a].shape._mdf = !0,
            this.shapes[a].shape.paths = this.shapes[a].localShapeCollection,
            this._mdf && (this.shapes[a].pathsData.length = 0);
    else if (1 === s && 0 === e || 0 === s && 1 === e) {
      if (this._mdf)
        for (a = 0; a < d; a += 1)
          this.shapes[a].pathsData.length = 0, this.shapes[a].shape._mdf = !0
    } else {
      var c, u, g = [];
      for (a = 0; a < d; a += 1)
        if ((c = this.shapes[a]).shape._mdf || this._mdf || t || 2 === this.m) {
          if (o = (i = c.shape.paths)._length, f = 0,
              !c.shape._mdf && c.pathsData.length)
            f = c.totalShapeLength;
          else {
            for (l = this.releasePathsData(c.pathsData), h = 0; h < o; h += 1)
              p = dt.getSegmentsLength(i.shapes[h]), l.push(p),
              f += p.totalLength;
            c.totalShapeLength = f, c.pathsData = l
          }
          m += f, c.shape._mdf = !0
        } else
          c.shape.paths = c.localShapeCollection;
      var y, v = e, b = s, _ = 0;
      for (a = d - 1; 0 <= a; a -= 1)
        if ((c = this.shapes[a]).shape._mdf) {
          for ((u = c.localShapeCollection).releaseShapes(),
               2 === this.m && 1 < d ? (y = this.calculateShapeEdges(
                                            e, s, c.totalShapeLength, _, m),
                                       _ += c.totalShapeLength) :
                                       y = [[v, b]],
                                       o = y.length, h = 0;
               h < o; h += 1) {
            v = y[h][0], b = y[h][1], g.length = 0,
            b <= 1 ?
                g.push({s: c.totalShapeLength * v, e: c.totalShapeLength * b}) :
                1 <= v ?
                g.push({
                  s: c.totalShapeLength * (v - 1),
                  e: c.totalShapeLength * (b - 1)
                }) :
                (g.push({s: c.totalShapeLength * v, e: c.totalShapeLength}),
                 g.push({s: 0, e: c.totalShapeLength * (b - 1)}));
            var k = this.addShapes(c, g[0]);
            if (g[0].s !== g[0].e) {
              if (1 < g.length)
                if (c.shape.paths.shapes[c.shape.paths._length - 1].c) {
                  var A = k.pop();
                  this.addPaths(k, u), k = this.addShapes(c, g[1], A)
                } else
                  this.addPaths(k, u), k = this.addShapes(c, g[1]);
              this.addPaths(k, u)
            }
          }
          c.shape.paths = u
        }
    }
  },
  K.prototype.addPaths =
      function(t, e) {
    var s, i = t.length;
    for (s = 0; s < i; s += 1) e.addShape(t[s])
  },
  K.prototype.addSegment =
      function(t, e, s, i, a, r, n) {
    a.setXYAt(e[0], e[1], 'o', r), a.setXYAt(s[0], s[1], 'i', r + 1),
        n && a.setXYAt(t[0], t[1], 'v', r), a.setXYAt(i[0], i[1], 'v', r + 1)
  },
  K.prototype.addSegmentFromArray =
      function(t, e, s, i) {
    e.setXYAt(t[1], t[5], 'o', s), e.setXYAt(t[2], t[6], 'i', s + 1),
        i && e.setXYAt(t[0], t[4], 'v', s), e.setXYAt(t[3], t[7], 'v', s + 1)
  },
  K.prototype.addShapes =
      function(t, e, s) {
    var i, a, r, n, h, o, l, p, f = t.pathsData, d = t.shape.paths.shapes,
                                m = t.shape.paths._length, c = 0, u = [],
                                g = !0;
    for (p = s ? (h = s._length, s._length) : (s = Dt.newElement(), h = 0),
        u.push(s), i = 0;
         i < m; i += 1) {
      for (o = f[i].lengths, s.c = d[i].c, r = d[i].c ? o.length : o.length + 1,
          a = 1;
           a < r; a += 1)
        if (c + (n = o[a - 1]).addedLength < e.s)
          c += n.addedLength, s.c = !1;
        else {
          if (c > e.e) {
            s.c = !1;
            break
          }
          e.s <= c && e.e >= c + n.addedLength ?
              (this.addSegment(
                   d[i].v[a - 1], d[i].o[a - 1], d[i].i[a], d[i].v[a], s, h, g),
               g = !1) :
              (l = dt.getNewSegment(
                   d[i].v[a - 1], d[i].v[a], d[i].o[a - 1], d[i].i[a],
                   (e.s - c) / n.addedLength, (e.e - c) / n.addedLength,
                   o[a - 1]),
               this.addSegmentFromArray(l, s, h, g), g = !1, s.c = !1),
              c += n.addedLength, h += 1
        }
      if (d[i].c && o.length) {
        if (n = o[a - 1], c <= e.e) {
          var y = o[a - 1].addedLength;
          e.s <= c && e.e >= c + y ?
              (this.addSegment(
                   d[i].v[a - 1], d[i].o[a - 1], d[i].i[0], d[i].v[0], s, h, g),
               g = !1) :
              (l = dt.getNewSegment(
                   d[i].v[a - 1], d[i].v[0], d[i].o[a - 1], d[i].i[0],
                   (e.s - c) / y, (e.e - c) / y, o[a - 1]),
               this.addSegmentFromArray(l, s, h, g), g = !1, s.c = !1)
        } else
          s.c = !1;
        c += n.addedLength, h += 1
      }
      if (s._length &&
              (s.setXYAt(s.v[p][0], s.v[p][1], 'i', p),
               s.setXYAt(
                   s.v[s._length - 1][0], s.v[s._length - 1][1], 'o',
                   s._length - 1)),
          c > e.e)
        break;
      i < m - 1 && (s = Dt.newElement(), g = !0, u.push(s), h = 0)
    }
    return u
  },
  Y.registerModifier('tm', K), M([G], J),
  J.prototype.initModifierProperties =
      function(t, e) {
    this.getValue = this.processKeys,
    this.rd = R.getProp(t, e.r, 0, null, this),
    this._isAnimated = !!this.rd.effectsSequence.length
  },
  J.prototype.processPath =
      function(t, e) {
    var s, i = Dt.newElement();
    i.c = t.c;
    var a, r, n, h, o, l, p, f, d, m, c, u, g = t._length, y = 0;
    for (s = 0; s < g; s += 1)
      a = t.v[s], n = t.o[s], r = t.i[s],
      a[0] === n[0] && a[1] === n[1] && a[0] === r[0] && a[1] === r[1] ?
          0 !== s && s !== g - 1 || t.c ?
          (h = 0 === s ? t.v[g - 1] : t.v[s - 1],
           l = (o = Math.sqrt(
                    Math.pow(a[0] - h[0], 2) + Math.pow(a[1] - h[1], 2))) ?
               Math.min(o / 2, e) / o :
               0,
           p = c = a[0] + (h[0] - a[0]) * l, f = u = a[1] - (a[1] - h[1]) * l,
           d = p - (p - a[0]) * v, m = f - (f - a[1]) * v,
           i.setTripleAt(p, f, d, m, c, u, y), y += 1,
           h = s === g - 1 ? t.v[0] : t.v[s + 1],
           l = (o = Math.sqrt(
                    Math.pow(a[0] - h[0], 2) + Math.pow(a[1] - h[1], 2))) ?
               Math.min(o / 2, e) / o :
               0,
           p = d = a[0] + (h[0] - a[0]) * l, f = m = a[1] + (h[1] - a[1]) * l,
           c = p - (p - a[0]) * v, u = f - (f - a[1]) * v,
           i.setTripleAt(p, f, d, m, c, u, y)) :
          i.setTripleAt(a[0], a[1], n[0], n[1], r[0], r[1], y) :
          i.setTripleAt(
              t.v[s][0], t.v[s][1], t.o[s][0], t.o[s][1], t.i[s][0], t.i[s][1],
              y),
      y += 1;
    return i
  },
  J.prototype.processShapes =
      function(t) {
    var e, s, i, a, r, n, h = this.shapes.length, o = this.rd.v;
    if (0 !== o)
      for (s = 0; s < h; s += 1) {
        if (n = (r = this.shapes[s]).localShapeCollection,
            r.shape._mdf || this._mdf || t)
          for (n.releaseShapes(), r.shape._mdf = !0, e = r.shape.paths.shapes,
                                  a = r.shape.paths._length, i = 0;
               i < a; i += 1)
            n.addShape(this.processPath(e[i], o));
        r.shape.paths = r.localShapeCollection
      }
    this.dynamicProperties.length || (this._mdf = !1)
  },
  Y.registerModifier('rd', J), M([G], U),
  U.prototype.initModifierProperties =
      function(t, e) {
    this.getValue = this.processKeys,
    this.amount = R.getProp(t, e.a, 0, null, this),
    this._isAnimated = !!this.amount.effectsSequence.length
  },
  U.prototype.processPath =
      function(t, e) {
    var s = e / 100, i = [0, 0], a = t._length, r = 0;
    for (r = 0; r < a; r += 1) i[0] += t.v[r][0], i[1] += t.v[r][1];
    i[0] /= a, i[1] /= a;
    var n, h, o, l, p, f, d = Dt.newElement();
    for (d.c = t.c, r = 0; r < a; r += 1)
      n = t.v[r][0] + (i[0] - t.v[r][0]) * s,
      h = t.v[r][1] + (i[1] - t.v[r][1]) * s,
      o = t.o[r][0] + (i[0] - t.o[r][0]) * -s,
      l = t.o[r][1] + (i[1] - t.o[r][1]) * -s,
      p = t.i[r][0] + (i[0] - t.i[r][0]) * -s,
      f = t.i[r][1] + (i[1] - t.i[r][1]) * -s,
      d.setTripleAt(n, h, o, l, p, f, r);
    return d
  },
  U.prototype.processShapes =
      function(t) {
    var e, s, i, a, r, n, h = this.shapes.length, o = this.amount.v;
    if (0 !== o)
      for (s = 0; s < h; s += 1) {
        if (n = (r = this.shapes[s]).localShapeCollection,
            r.shape._mdf || this._mdf || t)
          for (n.releaseShapes(), r.shape._mdf = !0, e = r.shape.paths.shapes,
                                  a = r.shape.paths._length, i = 0;
               i < a; i += 1)
            n.addShape(this.processPath(e[i], o));
        r.shape.paths = r.localShapeCollection
      }
    this.dynamicProperties.length || (this._mdf = !1)
  },
  Y.registerModifier('pb', U), M([G], Z),
  Z.prototype.initModifierProperties = function(t, e) {
    this.getValue = this.processKeys, this.c = R.getProp(t, e.c, 0, null, this),
    this.o = R.getProp(t, e.o, 0, null, this),
    this.tr = z.getTransformProperty(t, e.tr, this),
    this.so = R.getProp(t, e.tr.so, 0, .01, this),
    this.eo = R.getProp(t, e.tr.eo, 0, .01, this), this.data = e,
    this.dynamicProperties.length || this.getValue(!0),
    this._isAnimated = !!this.dynamicProperties.length, this.pMatrix = new I,
    this.rMatrix = new I, this.sMatrix = new I, this.tMatrix = new I,
    this.matrix = new I
  }, Z.prototype.applyTransforms = function(t, e, s, i, a, r) {
    var n = r ? -1 : 1, h = i.s.v[0] + (1 - i.s.v[0]) * (1 - a),
        o = i.s.v[1] + (1 - i.s.v[1]) * (1 - a);
    t.translate(i.p.v[0] * n * a, i.p.v[1] * n * a, i.p.v[2]),
        e.translate(-i.a.v[0], -i.a.v[1], i.a.v[2]), e.rotate(-i.r.v * n * a),
        e.translate(i.a.v[0], i.a.v[1], i.a.v[2]),
        s.translate(-i.a.v[0], -i.a.v[1], i.a.v[2]),
        s.scale(r ? 1 / h : h, r ? 1 / o : o),
        s.translate(i.a.v[0], i.a.v[1], i.a.v[2])
  }, Z.prototype.init = function(t, e, s, i) {
    for (this.elem = t, this.arr = e, this.pos = s, this.elemsData = i,
        this._currentCopies = 0, this._elements = [], this._groups = [],
        this.frameId = -1, this.initDynamicPropertyContainer(t),
        this.initModifierProperties(t, e[s]);
         0 < s;)
      s -= 1, this._elements.unshift(e[s]);
    this.dynamicProperties.length ? this.k = !0 : this.getValue(!0)
  }, Z.prototype.resetElements = function(t) {
    var e, s = t.length;
    for (e = 0; e < s; e += 1)
      t[e]._processed = !1, 'gr' === t[e].ty && this.resetElements(t[e].it)
  }, Z.prototype.cloneElements = function(t) {
    var e = JSON.parse(JSON.stringify(t));
    return this.resetElements(e), e
  }, Z.prototype.changeGroupRender = function(t, e) {
    var s, i = t.length;
    for (s = 0; s < i; s += 1)
      t[s]._render = e, 'gr' === t[s].ty && this.changeGroupRender(t[s].it, e)
  }, Z.prototype.processShapes = function(t) {
    var e, s, i, a, r, n = !1;
    if (this._mdf || t) {
      var h, o = Math.ceil(this.c.v);
      if (this._groups.length < o) {
        for (; this._groups.length < o;) {
          var l = {it: this.cloneElements(this._elements), ty: 'gr'};
          l.it.push({
            a: {a: 0, ix: 1, k: [0, 0]},
            nm: 'Transform',
            o: {a: 0, ix: 7, k: 100},
            p: {a: 0, ix: 2, k: [0, 0]},
            r: {a: 1, ix: 6, k: [{s: 0, e: 0, t: 0}, {s: 0, e: 0, t: 1}]},
            s: {a: 0, ix: 3, k: [100, 100]},
            sa: {a: 0, ix: 5, k: 0},
            sk: {a: 0, ix: 4, k: 0},
            ty: 'tr'
          }),
              this.arr.splice(0, 0, l), this._groups.splice(0, 0, l),
              this._currentCopies += 1
        }
        this.elem.reloadShapes(), n = !0
      }
      for (i = r = 0; i <= this._groups.length - 1; i += 1) {
        if (h = r < o, this._groups[i]._render = h,
            this.changeGroupRender(this._groups[i].it, h), !h) {
          var p = this.elemsData[i].it, f = p[p.length - 1];
          0 !== f.transform.op.v ?
              (f.transform.op._mdf = !0, f.transform.op.v = 0) :
              f.transform.op._mdf = !1
        }
        r += 1
      }
      this._currentCopies = o;
      var d = this.o.v, m = d % 1, c = 0 < d ? Math.floor(d) : Math.ceil(d),
          u = this.pMatrix.props, g = this.rMatrix.props,
          y = this.sMatrix.props;
      this.pMatrix.reset(), this.rMatrix.reset(), this.sMatrix.reset(),
          this.tMatrix.reset(), this.matrix.reset();
      var v, b, _ = 0;
      if (0 < d) {
        for (; _ < c;)
          this.applyTransforms(
              this.pMatrix, this.rMatrix, this.sMatrix, this.tr, 1, !1),
              _ += 1;
        m &&
            (this.applyTransforms(
                 this.pMatrix, this.rMatrix, this.sMatrix, this.tr, m, !1),
             _ += m)
      } else if (d < 0) {
        for (; c < _;)
          this.applyTransforms(
              this.pMatrix, this.rMatrix, this.sMatrix, this.tr, 1, !0),
              _ -= 1;
        m &&
            (this.applyTransforms(
                 this.pMatrix, this.rMatrix, this.sMatrix, this.tr, -m, !0),
             _ -= m)
      }
      for (i = 1 === this.data.m ? 0 : this._currentCopies - 1,
          a = 1 === this.data.m ? 1 : -1, r = this._currentCopies;
           r;) {
        if (b = (s = (e = this.elemsData[i].it)[e.length - 1]
                         .transform.mProps.v.props)
                    .length,
            e[e.length - 1].transform.mProps._mdf = !0,
            e[e.length - 1].transform.op._mdf = !0,
            e[e.length - 1].transform.op.v = 1 === this._currentCopies ?
                this.so.v :
                this.so.v +
                    (this.eo.v - this.so.v) * (i / (this._currentCopies - 1)),
            0 !== _) {
          for ((0 !== i && 1 === a ||
                i !== this._currentCopies - 1 && -1 === a) &&
                   this.applyTransforms(
                       this.pMatrix, this.rMatrix, this.sMatrix, this.tr, 1,
                       !1),
               this.matrix.transform(
                   g[0], g[1], g[2], g[3], g[4], g[5], g[6], g[7], g[8], g[9],
                   g[10], g[11], g[12], g[13], g[14], g[15]),
               this.matrix.transform(
                   y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8], y[9],
                   y[10], y[11], y[12], y[13], y[14], y[15]),
               this.matrix.transform(
                   u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], u[9],
                   u[10], u[11], u[12], u[13], u[14], u[15]),
               v = 0;
               v < b; v += 1)
            s[v] = this.matrix.props[v];
          this.matrix.reset()
        } else
          for (this.matrix.reset(), v = 0; v < b; v += 1)
            s[v] = this.matrix.props[v];
        _ += 1, r -= 1, i += a
      }
    } else
      for (r = this._currentCopies, i = 0, a = 1; r;)
        s = (e = this.elemsData[i].it)[e.length - 1].transform.mProps.v.props,
        e[e.length - 1].transform.mProps._mdf = !1,
        e[e.length - 1].transform.op._mdf = !1, r -= 1, i += a;
    return n
  }, Z.prototype.addShape = function() {
  }, Y.registerModifier('rp', Z), Q.prototype.addShape = function(t) {
    this._length === this._maxLength &&
        (this.shapes = this.shapes.concat(D(this._maxLength)),
         this._maxLength *= 2),
        this.shapes[this._length] = t, this._length += 1
  }, Q.prototype.releaseShapes = function() {
    var t;
    for (t = 0; t < this._length; t += 1) Dt.release(this.shapes[t]);
    this._length = 0
  }, $.prototype.getValue = function(t) {
    if ((this.elem.globalData.frameId !== this.frameId || t) &&
        (this.frameId = this.elem.globalData.frameId,
         this.iterateDynamicProperties(), this._mdf = this._mdf || t,
         this._mdf)) {
      var e = 0, s = this.dataProps.length;
      for ('svg' === this.renderer && (this.dashStr = ''), e = 0; e < s; e += 1)
        'o' !== this.dataProps[e].n ?
            'svg' === this.renderer ?
            this.dashStr += ' ' + this.dataProps[e].p.v :
            this.dashArray[e] = this.dataProps[e].p.v :
            this.dashoffset[0] = this.dataProps[e].p.v
    }
  }, M([F], $), tt.prototype.comparePoints = function(t, e) {
    for (var s = 0, i = this.o.length / 2; s < i;) {
      if (.01 < Math.abs(t[4 * s] - t[4 * e + 2 * s])) return !1;
      s += 1
    }
    return !0
  }, tt.prototype.checkCollapsable = function() {
    if (this.o.length / 2 != this.c.length / 4) return !1;
    if (this.data.k.k[0].s)
      for (var t = 0, e = this.data.k.k.length; t < e;) {
        if (!this.comparePoints(this.data.k.k[t].s, this.data.p)) return !1;
        t += 1
      }
    else if (!this.comparePoints(this.data.k.k, this.data.p))
      return !1;
    return !0
  }, tt.prototype.getValue = function(t) {
    if (this.prop.getValue(), this._mdf = !1, this._cmdf = !1, this._omdf = !1,
        this.prop._mdf || t) {
      var e, s, i, a = 4 * this.data.p;
      for (e = 0; e < a; e += 1)
        s = e % 4 == 0 ? 100 : 255, i = Math.round(this.prop.v[e] * s),
        this.c[e] !== i && (this.c[e] = i, this._cmdf = !t);
      if (this.o.length)
        for (a = this.prop.v.length, e = 4 * this.data.p; e < a; e += 1)
          s = e % 2 == 0 ? 100 : 1,
          i = e % 2 == 0 ? Math.round(100 * this.prop.v[e]) : this.prop.v[e],
          this.o[e - 4 * this.data.p] !== i &&
              (this.o[e - 4 * this.data.p] = i, this._omdf = !t);
      this._mdf = !t
    }
  }, M([F], tt);
  var et, st,
      it =
          function(t, e, s, i) {
        if (0 === e) return '';
        var a, r = t.o, n = t.i, h = t.v,
               o = ' M' + i.applyToPointStringified(h[0][0], h[0][1]);
        for (a = 1; a < e; a += 1)
          o += ' C' + i.applyToPointStringified(r[a - 1][0], r[a - 1][1]) +
              ' ' + i.applyToPointStringified(n[a][0], n[a][1]) + ' ' +
              i.applyToPointStringified(h[a][0], h[a][1]);
        return s && e &&
                   (o += ' C' +
                        i.applyToPointStringified(r[a - 1][0], r[a - 1][1]) +
                        ' ' + i.applyToPointStringified(n[0][0], n[0][1]) +
                        ' ' + i.applyToPointStringified(h[0][0], h[0][1]),
                    o += 'z'),
               o
      },
      at =
          function() {
        function t(t) {
          this.audios = [], this.audioFactory = t, this._volume = 1,
          this._isMuted = !1
        }
        return t.prototype = {
          addAudio: function(t) {
            this.audios.push(t)
          },
          pause: function() {
            var t, e = this.audios.length;
            for (t = 0; t < e; t += 1) this.audios[t].pause()
          },
          resume: function() {
            var t, e = this.audios.length;
            for (t = 0; t < e; t += 1) this.audios[t].resume()
          },
          setRate: function(t) {
            var e, s = this.audios.length;
            for (e = 0; e < s; e += 1) this.audios[e].setRate(t)
          },
          createAudio: function(t) {
            return this.audioFactory ? this.audioFactory(t) :
                Howl                 ? new Howl({src: [t]}) :
                                       {
                         isPlaying: !1,
                         play: function() {
                           this.isPlaying = !0
                         },
                         seek: function() {
                           this.isPlaying = !1
                         },
                         playing: function() {},
                         rate: function() {},
                         setVolume: function() {}
                       }
          },
          setAudioFactory: function(t) {
            this.audioFactory = t
          },
          setVolume: function(t) {
            this._volume = t, this._updateVolume()
          },
          mute: function() {
            this._isMuted = !0, this._updateVolume()
          },
          unmute: function() {
            this._isMuted = !1, this._updateVolume()
          },
          getVolume: function() {
            return this._volume
          },
          _updateVolume: function() {
            var t, e = this.audios.length;
            for (t = 0; t < e; t += 1)
              this.audios[t].volume(this._volume * (this._isMuted ? 0 : 1))
          }
        },
               function() {
                 return new t
               }
      }(),
      rt =
          function() {
        var a = function() {
          var t = w('canvas');
          t.width = 1, t.height = 1;
          var e = t.getContext('2d');
          return e.fillStyle = 'rgba(0,0,0,0)', e.fillRect(0, 0, 1, 1), t
        }();
        function t() {
          this.loadedAssets += 1,
              this.loadedAssets === this.totalImages &&
              this.loadedFootagesCount === this.totalFootages &&
              this.imagesLoadedCb && this.imagesLoadedCb(null)
        }
        function e() {
          this.loadedFootagesCount += 1,
              this.loadedAssets === this.totalImages &&
              this.loadedFootagesCount === this.totalFootages &&
              this.imagesLoadedCb && this.imagesLoadedCb(null)
        }
        function r(t, e, s) {
          var i = '';
          if (t.e)
            i = t.p;
          else if (e) {
            var a = t.p;
            -1 !== a.indexOf('images/') && (a = a.split('/')[1]), i = e + a
          } else
            i = s, i += t.u ? t.u : '', i += t.p;
          return i
        }
        function s() {
          this._imageLoaded = t.bind(this), this._footageLoaded = e.bind(this),
          this.testImageLoaded =
              function(t) {
            var e = 0, s = setInterval(function() {
                         (t.getBBox().width || 500 < e) &&
                             (this._imageLoaded(), clearInterval(s)),
                             e += 1
                       }.bind(this), 50)
          }.bind(this),
          this.createFootageData =
              function(t) {
            var e = {assetData: t}, s = r(t, this.assetsPath, this.path);
            return ot.load(
                       s,
                       function(t) {
                         e.img = t, this._footageLoaded()
                       }.bind(this),
                       function() {
                         e.img = {}, this._footageLoaded()
                       }.bind(this)),
                   e
          }.bind(this),
          this.assetsPath = '', this.path = '', this.totalImages = 0,
          this.totalFootages = 0, this.loadedAssets = 0,
          this.loadedFootagesCount = 0, this.imagesLoadedCb = null,
          this.images = []
        }
        return s.prototype = {
          loadAssets: function(t, e) {
            var s;
            this.imagesLoadedCb = e;
            var i = t.length;
            for (s = 0; s < i; s += 1)
              t[s].layers ||
                  (t[s].t ? 3 === t[s].t &&
                           (this.totalFootages += 1,
                            this.images.push(this.createFootageData(t[s]))) :
                            (this.totalImages += 1,
                             this.images.push(this._createImageData(t[s]))))
          },
          setAssetsPath: function(t) {
            this.assetsPath = t || ''
          },
          setPath: function(t) {
            this.path = t || ''
          },
          loadedImages: function() {
            return this.totalImages === this.loadedAssets
          },
          loadedFootages: function() {
            return this.totalFootages === this.loadedFootagesCount
          },
          destroy: function() {
            this.imagesLoadedCb = null, this.images.length = 0
          },
          getAsset: function(t) {
            for (var e = 0, s = this.images.length; e < s;) {
              if (this.images[e].assetData === t) return this.images[e].img;
              e += 1
            }
            return null
          },
          createImgData: function(t) {
            var e = r(t, this.assetsPath, this.path), s = w('img');
            s.crossOrigin = 'anonymous',
            s.addEventListener('load', this._imageLoaded, !1),
            s.addEventListener('error', function() {
              i.img = a, this._imageLoaded()
            }.bind(this), !1), s.src = e;
            var i = {img: s, assetData: t};
            return i
          },
          createImageData: function(t) {
            var e = r(t, this.assetsPath, this.path), s = x('image');
            n ? this.testImageLoaded(s) :
                s.addEventListener('load', this._imageLoaded, !1),
                s.addEventListener(
                    'error',
                    function() {
                      i.img = a, this._imageLoaded()
                    }.bind(this),
                    !1),
                s.setAttributeNS('http://www.w3.org/1999/xlink', 'href', e),
                this._elementHelper.append ? this._elementHelper.append(s) :
                                             this._elementHelper.appendChild(s);
            var i = {img: s, assetData: t};
            return i
          },
          imageLoaded: t,
          footageLoaded: e,
          setCacheType: function(t, e) {
            this._createImageData = 'svg' === t ?
                (this._elementHelper = e, this.createImageData.bind(this)) :
                this.createImgData.bind(this)
          }
        },
               s
      }(),
      nt =
          (et = {maskType: !0},
           (/MSIE 10/i.test(navigator.userAgent) ||
            /MSIE 9/i.test(navigator.userAgent) ||
            /rv:11.0/i.test(navigator.userAgent) ||
            /Edge\/\d./i.test(navigator.userAgent)) &&
               (et.maskType = !1),
           et),
      ht =
          ((st = {}).createFilter =
               function(t, e) {
                 var s = x('filter');
                 return s.setAttribute('id', t),
                        !0 !== e &&
                            (s.setAttribute('filterUnits', 'objectBoundingBox'),
                             s.setAttribute('x', '0%'),
                             s.setAttribute('y', '0%'),
                             s.setAttribute('width', '100%'),
                             s.setAttribute('height', '100%')),
                        s
               },
           st.createAlphaToLuminanceFilter =
               function() {
                 var t = x('feColorMatrix');
                 return t.setAttribute('type', 'matrix'),
                        t.setAttribute('color-interpolation-filters', 'sRGB'),
                        t.setAttribute(
                            'values',
                            '0 0 0 1 0  0 0 0 1 0  0 0 0 1 0  0 0 0 1 1'),
                        t
               },
           st),
      ot = function() {
        function r(t) {
          return t.response && 'object' == typeof t.response ?
              t.response :
              t.response && 'string' == typeof t.response ?
              JSON.parse(t.response) :
              t.responseText ? JSON.parse(t.responseText) :
                               null
        }
        return {
          load: function(t, e, s) {
            var i, a = new XMLHttpRequest;
            try {
              a.responseType = 'json'
            } catch (t) {
            }
            a.onreadystatechange = function() {
              if (4 === a.readyState)
                if (200 === a.status)
                  i = r(a), e(i);
                else
                  try {
                    i = r(a), e(i)
                  } catch (t) {
                    s && s(t)
                  }
            }, a.open('GET', t, !0), a.send()
          }
        }
      }();
  function mt(t, e, s) {
    this._isFirstFrame = !0, this._hasMaskedPath = !1, this._frameId = -1,
    this._textData = t, this._renderType = e, this._elem = s,
    this._animatorsData = D(this._textData.a.length), this._pathData = {},
    this._moreOptions = {alignment: {}}, this.renderedLetters = [],
    this.lettersChangedFlag = !1, this.initDynamicPropertyContainer(s)
  }
  function ct(t, e, s) {
    var i = {propType: !1}, a = R.getProp, r = e.a;
    this.a = {
      r: r.r ? a(t, r.r, 0, B, s) : i,
      rx: r.rx ? a(t, r.rx, 0, B, s) : i,
      ry: r.ry ? a(t, r.ry, 0, B, s) : i,
      sk: r.sk ? a(t, r.sk, 0, B, s) : i,
      sa: r.sa ? a(t, r.sa, 0, B, s) : i,
      s: r.s ? a(t, r.s, 1, .01, s) : i,
      a: r.a ? a(t, r.a, 1, 0, s) : i,
      o: r.o ? a(t, r.o, 0, .01, s) : i,
      p: r.p ? a(t, r.p, 1, 0, s) : i,
      sw: r.sw ? a(t, r.sw, 0, 0, s) : i,
      sc: r.sc ? a(t, r.sc, 1, 0, s) : i,
      fc: r.fc ? a(t, r.fc, 1, 0, s) : i,
      fh: r.fh ? a(t, r.fh, 0, 0, s) : i,
      fs: r.fs ? a(t, r.fs, 0, .01, s) : i,
      fb: r.fb ? a(t, r.fb, 0, .01, s) : i,
      t: r.t ? a(t, r.t, 0, 0, s) : i
    },
    this.s = At.getTextSelectorProp(t, e.s, s), this.s.t = e.s.t
  }
  function ut(t, e, s, i, a, r) {
    this.o = t, this.sw = e, this.sc = s, this.fc = i, this.m = a, this.p = r,
    this._mdf = {
      o: !0,
      sw: !!e,
      sc: !!s,
      fc: !!i,
      m: !0,
      p: !0
    }
  }
  function gt(t, e) {
    this._frameId = s, this.pv = '', this.v = '', this.kf = !1,
    this._isFirstFrame = !0, this._mdf = !1, this.data = e, this.elem = t,
    this.comp = this.elem.comp, this.keysIndex = 0, this.canResize = !1,
    this.minimumFontSize = 1, this.effectsSequence = [], this.currentData = {
      ascent: 0,
      boxWidth: this.defaultBoxWidth,
      f: '',
      fStyle: '',
      fWeight: '',
      fc: '',
      j: '',
      justifyOffset: '',
      l: [],
      lh: 0,
      lineWidths: [],
      ls: '',
      of: '',
      s: '',
      sc: '',
      sw: 0,
      t: 0,
      tr: 0,
      sz: 0,
      ps: null,
      fillColorAnim: !1,
      strokeColorAnim: !1,
      strokeWidthAnim: !1,
      yOffset: 0,
      finalSize: 0,
      finalText: [],
      finalLineHeight: 0,
      __complete: !1
    },
    this.copyData(this.currentData, this.data.d.k[0].s),
    this.searchProperty() || this.completeTextData(this.currentData)
  }
  mt.prototype.searchProperties =
      function() {
    var t, e, s = this._textData.a.length, i = R.getProp;
    for (t = 0; t < s; t += 1)
      e = this._textData.a[t],
      this._animatorsData[t] = new ct(this._elem, e, this);
    this._textData.p && 'm' in this._textData.p ?
        (this._pathData = {
          f: i(this._elem, this._textData.p.f, 0, 0, this),
          l: i(this._elem, this._textData.p.l, 0, 0, this),
          r: this._textData.p.r,
          m: this._elem.maskManager.getMaskProperty(this._textData.p.m)
        },
         this._hasMaskedPath = !0) :
        this._hasMaskedPath = !1,
        this._moreOptions.alignment =
            i(this._elem, this._textData.m.a, 1, 0, this)
  },
  mt.prototype.getMeasures =
      function(t, e) {
    if (this.lettersChangedFlag = e,
        this._mdf || this._isFirstFrame || e ||
            this._hasMaskedPath && this._pathData.m._mdf) {
      this._isFirstFrame = !1;
      var s, i, a, r, n, h, o, l, p, f, d, m, c, u, g, y, v, b, _,
          k = this._moreOptions.alignment.v, A = this._animatorsData,
          P = this._textData, S = this.mHelper, C = this._renderType,
          D = this.renderedLetters.length, x = t.l;
      if (this._hasMaskedPath) {
        if (_ = this._pathData.m, !this._pathData.n || this._pathData._mdf) {
          var w, F = _.v;
          for (this._pathData.r && (F = F.reverse()),
               n = {tLength: 0, segments: []}, r = F._length - 1, a = y = 0;
               a < r; a += 1)
            w = dt.buildBezierData(
                F.v[a], F.v[a + 1],
                [F.o[a][0] - F.v[a][0], F.o[a][1] - F.v[a][1]],
                [F.i[a + 1][0] - F.v[a + 1][0], F.i[a + 1][1] - F.v[a + 1][1]]),
            n.tLength += w.segmentLength, n.segments.push(w),
            y += w.segmentLength;
          a = r,
          _.v.c &&
              (w = dt.buildBezierData(
                   F.v[a], F.v[0],
                   [F.o[a][0] - F.v[a][0], F.o[a][1] - F.v[a][1]],
                   [F.i[0][0] - F.v[0][0], F.i[0][1] - F.v[0][1]]),
               n.tLength += w.segmentLength, n.segments.push(w),
               y += w.segmentLength),
          this._pathData.pi = n
        }
        if (n = this._pathData.pi, h = this._pathData.f.v, f = 1,
            p = !(l = d = 0), u = n.segments, h < 0 && _.v.c)
          for (n.tLength < Math.abs(h) && (h = -Math.abs(h) % n.tLength),
               f = (c = u[d = u.length - 1].points).length - 1;
               h < 0;)
            h += c[f].partialLength,
                (f -= 1) < 0 && (f = (c = u[d -= 1].points).length - 1);
        m = (c = u[d].points)[f - 1], g = (o = c[f]).partialLength
      }
      r = x.length, i = s = 0;
      var T, E, M, I, L, V = 1.2 * t.finalSize * .714, R = !0;
      M = A.length;
      var z, N, O, q, B, j, W, X, H, Y, G, K, J = -1, U = h, Z = d, Q = f,
                                              $ = -1, tt = '',
                                              et = this.defaultPropsArray;
      if (2 === t.j || 1 === t.j) {
        var st = 0, it = 0, at = 2 === t.j ? -.5 : -1, rt = 0, nt = !0;
        for (a = 0; a < r; a += 1)
          if (x[a].n) {
            for (st && (st += it); rt < a;)
              x[rt].animatorJustifyOffset = st, rt += 1;
            nt = !(st = 0)
          } else {
            for (E = 0; E < M; E += 1)
              (T = A[E].a).t.propType &&
                  (nt && 2 === t.j && (it += T.t.v * at),
                   (L = A[E].s.getMult(x[a].anIndexes[E], P.a[E].s.totalChars))
                           .length ?
                       st += T.t.v * L[0]* at :
                       st += T.t.v * L * at);
            nt = !1
          }
        for (st && (st += it); rt < a;)
          x[rt].animatorJustifyOffset = st, rt += 1
      }
      for (a = 0; a < r; a += 1) {
        if (S.reset(), q = 1, x[a].n)
          s = 0, i += t.yOffset, i += R ? 1 : 0, h = U, R = !1,
          this._hasMaskedPath &&
              (f = Q, m = (c = u[d = Z].points)[f - 1],
               g = (o = c[f]).partialLength, l = 0),
          K = H = G = tt = '', et = this.defaultPropsArray;
        else {
          if (this._hasMaskedPath) {
            if ($ !== x[a].line) {
              switch (t.j) {
                case 1:
                  h += y - t.lineWidths[x[a].line];
                  break;
                case 2:
                  h += (y - t.lineWidths[x[a].line]) / 2
              }
              $ = x[a].line
            }
            J !== x[a].ind &&
                (x[J] && (h += x[J].extra), h += x[a].an / 2, J = x[a].ind),
                h += k[0] * x[a].an * .005;
            var ht = 0;
            for (E = 0; E < M; E += 1)
              (T = A[E].a).p.propType &&
                  ((L = A[E].s.getMult(x[a].anIndexes[E], P.a[E].s.totalChars))
                           .length ?
                       ht += T.p.v[0] * L[0] :
                       ht += T.p.v[0] * L),
                  T.a.propType &&
                  ((L = A[E].s.getMult(x[a].anIndexes[E], P.a[E].s.totalChars))
                           .length ?
                       ht += T.a.v[0] * L[0] :
                       ht += T.a.v[0] * L);
            for (p = !0; p;)
              h + ht <= l + g || !c ?
                  (v = (h + ht - l) / o.partialLength,
                   N = m.point[0] + (o.point[0] - m.point[0]) * v,
                   O = m.point[1] + (o.point[1] - m.point[1]) * v,
                   S.translate(-k[0] * x[a].an * .005, -k[1] * V * .01),
                   p = !1) :
                  c &&
                      (l += o.partialLength,
                       (f += 1) >= c.length &&
                           (f = 0,
                            c = u[d += 1] ? u[d].points :
                                _.v.c     ? u[d = f = 0].points :
                                            (l -= o.partialLength, null)),
                       c && (m = o, g = (o = c[f]).partialLength));
            z = x[a].an / 2 - x[a].add, S.translate(-z, 0, 0)
          } else
            z = x[a].an / 2 - x[a].add, S.translate(-z, 0, 0),
            S.translate(-k[0] * x[a].an * .005, -k[1] * V * .01, 0);
          for (E = 0; E < M; E += 1)
            (T = A[E].a).t.propType &&
                (L = A[E].s.getMult(x[a].anIndexes[E], P.a[E].s.totalChars),
                 0 === s && 0 === t.j ||
                     (this._hasMaskedPath ?
                          L.length ? h += T.t.v * L[0] : h += T.t.v* L :
                          L.length ? s += T.t.v * L[0] :
                                     s += T.t.v * L));
          for (t.strokeWidthAnim && (j = t.sw || 0),
               t.strokeColorAnim &&
                   (B = t.sc ? [t.sc[0], t.sc[1], t.sc[2]] : [0, 0, 0]),
               t.fillColorAnim && t.fc && (W = [t.fc[0], t.fc[1], t.fc[2]]),
               E = 0;
               E < M; E += 1)
            (T = A[E].a).a.propType &&
                ((L = A[E].s.getMult(x[a].anIndexes[E], P.a[E].s.totalChars))
                         .length ?
                     S.translate(
                         -T.a.v[0] * L[0], -T.a.v[1] * L[1], T.a.v[2] * L[2]) :
                     S.translate(-T.a.v[0] * L, -T.a.v[1] * L, T.a.v[2] * L));
          for (E = 0; E < M; E += 1)
            (T = A[E].a).s.propType &&
                ((L = A[E].s.getMult(x[a].anIndexes[E], P.a[E].s.totalChars))
                         .length ?
                     S.scale(
                         1 + (T.s.v[0] - 1) * L[0], 1 + (T.s.v[1] - 1) * L[1],
                         1) :
                     S.scale(
                         1 + (T.s.v[0] - 1) * L, 1 + (T.s.v[1] - 1) * L, 1));
          for (E = 0; E < M; E += 1) {
            if (T = A[E].a,
                L = A[E].s.getMult(x[a].anIndexes[E], P.a[E].s.totalChars),
                T.sk.propType &&
                    (L.length ? S.skewFromAxis(-T.sk.v * L[0], T.sa.v * L[1]) :
                                S.skewFromAxis(-T.sk.v * L, T.sa.v * L)),
                T.r.propType &&
                    (L.length ? S.rotateZ(-T.r.v * L[2]) :
                                S.rotateZ(-T.r.v * L)),
                T.ry.propType &&
                    (L.length ? S.rotateY(T.ry.v * L[1]) :
                                S.rotateY(T.ry.v * L)),
                T.rx.propType &&
                    (L.length ? S.rotateX(T.rx.v * L[0]) :
                                S.rotateX(T.rx.v * L)),
                T.o.propType &&
                    (L.length ? q += (T.o.v * L[0] - q) * L[0] :
                                q += (T.o.v * L - q) * L),
                t.strokeWidthAnim && T.sw.propType &&
                    (L.length ? j += T.sw.v * L[0] : j += T.sw.v * L),
                t.strokeColorAnim && T.sc.propType)
              for (X = 0; X < 3; X += 1)
                L.length ? B[X] += (T.sc.v[X] - B[X]) * L[0] :
                           B[X] += (T.sc.v[X] - B[X]) * L;
            if (t.fillColorAnim && t.fc) {
              if (T.fc.propType)
                for (X = 0; X < 3; X += 1)
                  L.length ? W[X] += (T.fc.v[X] - W[X]) * L[0] :
                             W[X] += (T.fc.v[X] - W[X]) * L;
              T.fh.propType &&
                  (W = L.length ? ft(W, T.fh.v * L[0]) : ft(W, T.fh.v * L)),
                  T.fs.propType &&
                  (W = L.length ? lt(W, T.fs.v * L[0]) : lt(W, T.fs.v * L)),
                  T.fb.propType &&
                  (W = L.length ? pt(W, T.fb.v * L[0]) : pt(W, T.fb.v * L))
            }
          }
          for (E = 0; E < M; E += 1)
            (T = A[E].a).p.propType &&
                (L = A[E].s.getMult(x[a].anIndexes[E], P.a[E].s.totalChars),
                 this._hasMaskedPath ?
                     L.length ?
                     S.translate(0, T.p.v[1] * L[0], -T.p.v[2] * L[1]) :
                     S.translate(0, T.p.v[1] * L, -T.p.v[2] * L) :
                     L.length ?
                     S.translate(
                         T.p.v[0] * L[0], T.p.v[1] * L[1], -T.p.v[2] * L[2]) :
                     S.translate(T.p.v[0] * L, T.p.v[1] * L, -T.p.v[2] * L));
          if (t.strokeWidthAnim && (H = j < 0 ? 0 : j),
              t.strokeColorAnim &&
                  (Y = 'rgb(' + Math.round(255 * B[0]) + ',' +
                       Math.round(255 * B[1]) + ',' + Math.round(255 * B[2]) +
                       ')'),
              t.fillColorAnim && t.fc &&
                  (G = 'rgb(' + Math.round(255 * W[0]) + ',' +
                       Math.round(255 * W[1]) + ',' + Math.round(255 * W[2]) +
                       ')'),
              this._hasMaskedPath) {
            if (S.translate(0, -t.ls), S.translate(0, k[1] * V * .01 + i, 0),
                P.p.p) {
              b = (o.point[1] - m.point[1]) / (o.point[0] - m.point[0]);
              var ot = 180 * Math.atan(b) / Math.PI;
              o.point[0] < m.point[0] && (ot += 180),
                  S.rotate(-ot * Math.PI / 180)
            }
            S.translate(N, O, 0), h -= k[0] * x[a].an * .005,
                x[a + 1] && J !== x[a + 1].ind &&
                (h += x[a].an / 2, h += .001 * t.tr * t.finalSize)
          } else {
            switch (S.translate(s, i, 0),
                    t.ps && S.translate(t.ps[0], t.ps[1] + t.ascent, 0), t.j) {
              case 1:
                S.translate(
                    x[a].animatorJustifyOffset + t.justifyOffset +
                        (t.boxWidth - t.lineWidths[x[a].line]),
                    0, 0);
                break;
              case 2:
                S.translate(
                    x[a].animatorJustifyOffset + t.justifyOffset +
                        (t.boxWidth - t.lineWidths[x[a].line]) / 2,
                    0, 0)
            }
            S.translate(0, -t.ls), S.translate(z, 0, 0),
                S.translate(k[0] * x[a].an * .005, k[1] * V * .01, 0),
                s += x[a].l + .001 * t.tr * t.finalSize
          }
          'html' === C ?
              tt = S.toCSS() :
              'svg' === C ?
              tt = S.to2dCSS() :
              et =
                  [
                    S.props[0], S.props[1], S.props[2], S.props[3], S.props[4],
                    S.props[5], S.props[6], S.props[7], S.props[8], S.props[9],
                    S.props[10], S.props[11], S.props[12], S.props[13],
                    S.props[14], S.props[15]
                  ],
              K = q
        }
        this.lettersChangedFlag = D <= a ?
            (I = new ut(K, H, Y, G, tt, et), this.renderedLetters.push(I),
             D += 1, !0) :
            (I = this.renderedLetters[a]).update(K, H, Y, G, tt, et) ||
                this.lettersChangedFlag
      }
    }
  },
  mt.prototype.getValue =
      function() {
    this._elem.globalData.frameId !== this._frameId &&
        (this._frameId = this._elem.globalData.frameId,
         this.iterateDynamicProperties())
  },
  mt.prototype.mHelper = new I, mt.prototype.defaultPropsArray = [], M([F], mt),
  ut.prototype.update =
      function(t, e, s, i, a, r) {
    this._mdf.o = !1, this._mdf.sw = !1, this._mdf.sc = !1, this._mdf.fc = !1,
    this._mdf.m = !1;
    var n = this._mdf.p = !1;
    return this.o !== t && (this.o = t, n = this._mdf.o = !0),
           this.sw !== e && (this.sw = e, n = this._mdf.sw = !0),
           this.sc !== s && (this.sc = s, n = this._mdf.sc = !0),
           this.fc !== i && (this.fc = i, n = this._mdf.fc = !0),
           this.m !== a && (this.m = a, n = this._mdf.m = !0),
           !r.length ||
               this.p[0] === r[0] && this.p[1] === r[1] && this.p[4] === r[4] &&
                   this.p[5] === r[5] && this.p[12] === r[12] &&
                   this.p[13] === r[13] ||
               (this.p = r, n = this._mdf.p = !0),
           n
  },
  gt.prototype.defaultBoxWidth = [0, 0],
  gt.prototype.copyData = function(t, e) {
    for (var s in e)
      Object.prototype.hasOwnProperty.call(e, s) && (t[s] = e[s]);
    return t
  }, gt.prototype.setCurrentData = function(t) {
    t.__complete || this.completeTextData(t),
        this.currentData = t,
        this.currentData.boxWidth =
            this.currentData.boxWidth || this.defaultBoxWidth,
        this._mdf = !0
  }, gt.prototype.searchProperty = function() {
    return this.searchKeyframes()
  }, gt.prototype.searchKeyframes = function() {
    return this.kf = 1 < this.data.d.k.length,
           this.kf && this.addEffect(this.getKeyframeValue.bind(this)), this.kf
  }, gt.prototype.addEffect = function(t) {
    this.effectsSequence.push(t), this.elem.addDynamicProperty(this)
  }, gt.prototype.getValue = function(t) {
    if (this.elem.globalData.frameId !== this.frameId &&
            this.effectsSequence.length ||
        t) {
      this.currentData.t = this.data.d.k[this.keysIndex].s.t;
      var e = this.currentData, s = this.keysIndex;
      if (this.lock)
        this.setCurrentData(this.currentData);
      else {
        var i;
        this.lock = !0, this._mdf = !1;
        var a = this.effectsSequence.length,
            r = t || this.data.d.k[this.keysIndex].s;
        for (i = 0; i < a; i += 1)
          r = s !== this.keysIndex ?
              this.effectsSequence[i](r, r.t) :
              this.effectsSequence[i](this.currentData, r.t);
        e !== r && this.setCurrentData(r),
            this.v = this.currentData, this.pv = this.v, this.lock = !1,
            this.frameId = this.elem.globalData.frameId
      }
    }
  }, gt.prototype.getKeyframeValue = function() {
    for (var t = this.data.d.k, e = this.elem.comp.renderedFrame, s = 0,
             i = t.length;
         s <= i - 1 && !(s === i - 1 || t[s + 1].t > e);)
      s += 1;
    return this.keysIndex !== s && (this.keysIndex = s),
           this.data.d.k[this.keysIndex].s
  }, gt.prototype.buildFinalText = function(t) {
    for (var e, s = V.getCombinedCharacterCodes(), i = [], a = 0, r = t.length;
         a < r;)
      e = t.charCodeAt(a),
      -1 !== s.indexOf(e) ? i[i.length - 1] += t.charAt(a) :
          55296 <= e && e <= 56319 && 56320 <= (e = t.charCodeAt(a + 1)) &&
              e <= 57343 ?
                            (i.push(t.substr(a, 2)), a += 1) :
                            i.push(t.charAt(a)),
      a += 1;
    return i
  }, gt.prototype.completeTextData = function(t) {
    t.__complete = !0;
    var e, s, i, a, r, n, h, o = this.elem.globalData.fontManager,
                             l = this.data, p = [], f = 0, d = l.m.g, m = 0,
                             c = 0, u = 0, g = [], y = 0, v = 0,
                             b = o.getFontByName(t.f), _ = 0, k = q(b);
    t.fWeight = k.weight, t.fStyle = k.style, t.finalSize = t.s,
    t.finalText = this.buildFinalText(t.t), s = t.finalText.length,
    t.finalLineHeight = t.lh;
    var A, P = t.tr / 1e3 * t.finalSize;
    if (t.sz)
      for (var S, C, D = !0, x = t.sz[0], w = t.sz[1]; D;) {
        y = S = 0, s = (C = this.buildFinalText(t.t)).length,
        P = t.tr / 1e3 * t.finalSize;
        var F = -1;
        for (e = 0; e < s; e += 1)
          A = C[e].charCodeAt(0), i = !1,
          ' ' === C[e] ? F = e :
                         13 !== A && 3 !== A ||
                  (i = !(y = 0), S += t.finalLineHeight || 1.2 * t.finalSize),
          x < y +
                          (_ = o.chars ?
                               (h = o.getCharData(C[e], b.fStyle, b.fFamily),
                                i ? 0 : h.w * t.finalSize / 100) :
                               o.measureText(C[e], t.f, t.finalSize)) &&
                  ' ' !== C[e] ?
              (-1 === F ? s += 1 : e = F,
               S += t.finalLineHeight || 1.2 * t.finalSize,
               C.splice(e, F === e ? 1 : 0, '\r'), F = -1, y = 0) :
              (y += _, y += P);
        S += b.ascent * t.finalSize / 100,
            this.canResize && t.finalSize > this.minimumFontSize && w < S ?
            (t.finalSize -= 1, t.finalLineHeight = t.finalSize * t.lh / t.s) :
            (t.finalText = C, s = t.finalText.length, D = !1)
      }
    y = -P;
    var T, E = _ = 0;
    for (e = 0; e < s; e += 1)
      if (i = !1,
          13 === (A = (T = t.finalText[e]).charCodeAt(0)) || 3 === A ?
              (E = 0, g.push(y), v = v < y ? y : v, y = -2 * P, i = !(a = ''),
               u += 1) :
              a = T,
          _ = o.chars ?
              (h = o.getCharData(T, b.fStyle, o.getFontByName(t.f).fFamily),
               i ? 0 : h.w * t.finalSize / 100) :
              o.measureText(a, t.f, t.finalSize),
          ' ' === T ? E += _ + P : (y += _ + P + E, E = 0), p.push({
            l: _,
            an: _,
            add: m,
            n: i,
            anIndexes: [],
            val: a,
            line: u,
            animatorJustifyOffset: 0
          }),
          2 == d) {
        if (m += _, '' === a || ' ' === a || e === s - 1) {
          for ('' !== a && ' ' !== a || (m -= _); c <= e;)
            p[c].an = m, p[c].ind = f, p[c].extra = _, c += 1;
          f += 1, m = 0
        }
      } else if (3 == d) {
        if (m += _, '' === a || e === s - 1) {
          for ('' === a && (m -= _); c <= e;)
            p[c].an = m, p[c].ind = f, p[c].extra = _, c += 1;
          m = 0, f += 1
        }
      } else
        p[f].ind = f, p[f].extra = 0, f += 1;
    if (t.l = p, v = v < y ? y : v, g.push(y), t.sz)
      t.boxWidth = t.sz[0], t.justifyOffset = 0;
    else
      switch (t.boxWidth = v, t.j) {
        case 1:
          t.justifyOffset = -t.boxWidth;
          break;
        case 2:
          t.justifyOffset = -t.boxWidth / 2;
          break;
        default:
          t.justifyOffset = 0
      }
    t.lineWidths = g;
    var M, I, L, V, R = l.a;
    n = R.length;
    var z = [];
    for (r = 0; r < n; r += 1) {
      for ((M = R[r]).a.sc && (t.strokeColorAnim = !0),
           M.a.sw && (t.strokeWidthAnim = !0),
           (M.a.fc || M.a.fh || M.a.fs || M.a.fb) && (t.fillColorAnim = !0),
           V = 0, L = M.s.b, e = 0;
           e < s; e += 1)
        (I = p[e]).anIndexes[r] = V,
             (1 == L && '' !== I.val ||
              2 == L && '' !== I.val && ' ' !== I.val ||
              3 == L && (I.n || ' ' == I.val || e == s - 1) ||
              4 == L && (I.n || e == s - 1)) &&
            (1 === M.s.rn && z.push(V), V += 1);
      l.a[r].s.totalChars = V;
      var N, O = -1;
      if (1 === M.s.rn)
        for (e = 0; e < s; e += 1)
          O != (I = p[e]).anIndexes[r] &&
              (O = I.anIndexes[r],
               N = z.splice(Math.floor(Math.random() * z.length), 1)[0]),
              I.anIndexes[r] = N
    }
    t.yOffset = t.finalLineHeight || 1.2 * t.finalSize, t.ls = t.ls || 0,
    t.ascent = b.ascent * t.finalSize / 100
  }, gt.prototype.updateDocumentData = function(t, e) {
    e = void 0 === e ? this.keysIndex : e;
    var s = this.copyData({}, this.data.d.k[e].s);
    s = this.copyData(s, t), this.data.d.k[e].s = s, this.recalculate(e),
    this.elem.addDynamicProperty(this)
  }, gt.prototype.recalculate = function(t) {
    var e = this.data.d.k[t].s;
    e.__complete = !1, this.keysIndex = 0, this._isFirstFrame = !0,
    this.getValue(e)
  }, gt.prototype.canResizeFont = function(t) {
    this.canResize = t, this.recalculate(this.keysIndex),
    this.elem.addDynamicProperty(this)
  }, gt.prototype.setMinimumFontSize = function(t) {
    this.minimumFontSize = Math.floor(t) || 1, this.recalculate(this.keysIndex),
    this.elem.addDynamicProperty(this)
  };
  var yt, vt, bt, _t, kt,
      At =
          function() {
        var m = Math.max, c = Math.min, u = Math.floor;
        function i(t, e) {
          this._currentTextLength = -1, this.k = !1, this.data = e,
          this.elem = t, this.comp = t.comp, this.finalS = 0, this.finalE = 0,
          this.initDynamicPropertyContainer(t),
          this.s = R.getProp(t, e.s || {k: 0}, 0, 0, this),
          this.e = 'e' in e ? R.getProp(t, e.e, 0, 0, this) : {v: 100},
          this.o = R.getProp(t, e.o || {k: 0}, 0, 0, this),
          this.xe = R.getProp(t, e.xe || {k: 0}, 0, 0, this),
          this.ne = R.getProp(t, e.ne || {k: 0}, 0, 0, this),
          this.a = R.getProp(t, e.a, 0, .01, this),
          this.dynamicProperties.length || this.getValue()
        }
        return i.prototype = {
          getMult: function(t) {
            this._currentTextLength !==
                    this.elem.textProperty.currentData.l.length &&
                this.getValue();
            var e = 0, s = 0, i = 1, a = 1;
            0 < this.ne.v ? e = this.ne.v / 100 : s = -this.ne.v / 100,
                            0 < this.xe.v ? i = 1 - this.xe.v / 100 :
                                            a = 1 + this.xe.v / 100;
            var r = W.getBezierEasing(e, s, i, a).get, n = 0, h = this.finalS,
                o = this.finalE, l = this.data.sh;
            if (2 === l)
              n =
                  r(n = o === h ? o <= t ? 1 : 0 :
                                  m(0, c(.5 / (o - h) + (t - h) / (o - h), 1)));
            else if (3 === l)
              n =
                  r(n = o === h ?
                        o <= t ? 0 : 1 :
                        1 - m(0, c(.5 / (o - h) + (t - h) / (o - h), 1)));
            else if (4 === l)
              o === h ? n = 0 :
                  (n = m(0, c(.5 / (o - h) + (t - h) / (o - h), 1))) < .5 ?
                        n *= 2 :
                        n = 1 - 2 * (n - .5),
                        n = r(n);
            else if (5 === l) {
              if (o === h)
                n = 0;
              else {
                var p = o - h, f = -p / 2 + (t = c(m(0, t + .5 - h), o - h)),
                    d = p / 2;
                n = Math.sqrt(1 - f * f / (d * d))
              }
              n = r(n)
            } else
              n = 6 === l ?
                  r(n = o === h ?
                        0 :
                        (t = c(m(0, t + .5 - h), o - h),
                         (1 + Math.cos(Math.PI + 2 * Math.PI * t / (o - h))) /
                             2)) :
                  (t >= u(h) &&
                       (n = m(0, c(t - h < 0 ? c(o, 1) - (h - t) : o - t, 1))),
                   r(n));
            return n * this.a.v
          },
          getValue: function(t) {
            this.iterateDynamicProperties(),
                this._mdf = t || this._mdf,
                this._currentTextLength =
                    this.elem.textProperty.currentData.l.length || 0,
                t && 2 === this.data.r && (this.e.v = this._currentTextLength);
            var e = 2 === this.data.r ? 1 : 100 / this.data.totalChars,
                s = this.o.v / e, i = this.s.v / e + s, a = this.e.v / e + s;
            if (a < i) {
              var r = i;
              i = a, a = r
            }
            this.finalS = i, this.finalE = a
          }
        },
               M([F], i), {
          getTextSelectorProp: function(t, e, s) {
            return new i(t, e, s)
          }
        }
      }(),
      Pt =
          function(t, e, s) {
        var i = 0, a = t, r = D(a);
        return {
          newElement: function() {
            return i ? r[i -= 1] : e()
          }, release: function(t) {
            i === a && (r = St.double(r), a *= 2), s && s(t), r[i] = t, i += 1
          }
        }
      },
      St = {
        double: function(t) {
          return t.concat(D(t.length))
        }
      },
      Ct =
          Pt(8,
             function() {
               return j('float32', 2)
             }),
      Dt =
          ((yt = Pt(
                4,
                function() {
                  return new N
                },
                function(t) {
                  var e, s = t._length;
                  for (e = 0; e < s; e += 1)
                    Ct.release(t.v[e]), Ct.release(t.i[e]), Ct.release(t.o[e]),
                        t.v[e] = null, t.i[e] = null, t.o[e] = null;
                  t._length = 0, t.c = !1
                }))
               .clone =
               function(t) {
                 var e, s = yt.newElement(),
                        i = void 0 === t._length ? t.v.length : t._length;
                 for (s.setLength(i), s.c = t.c, e = 0; e < i; e += 1)
                   s.setTripleAt(
                       t.v[e][0], t.v[e][1], t.o[e][0], t.o[e][1], t.i[e][0],
                       t.i[e][1], e);
                 return s
               },
           yt),
      xt =
          (vt = {
            newShapeCollection: function() {
              var t;
              t = bt ? kt[bt -= 1] : new Q;
              return t
            },
            release: function(t) {
              var e, s = t._length;
              for (e = 0; e < s; e += 1) Dt.release(t.shapes[e]);
              t._length = 0, bt === _t && (kt = St.double(kt), _t *= 2);
              kt[bt] = t, bt += 1
            }
          },
           bt = 0, kt = D(_t = 4), vt),
      wt =
          Pt(8,
             function() {
               return {
                 lengths: [], totalLength: 0
               }
             },
             function(t) {
               var e, s = t.lengths.length;
               for (e = 0; e < s; e += 1) Ft.release(t.lengths[e]);
               t.lengths.length = 0
             }),
      Ft = Pt(8, function() {
        return {
          addedLength: 0, percents: j('float32', P), lengths: j('float32', P)
        }
      }), Tt = function() {
        function r(t) {
          for (var e, s = t.split('\r\n'), i = {}, a = 0, r = 0; r < s.length;
               r += 1)
            2 === (e = s[r].split(':')).length &&
                (i[e[0]] = e[1].trim(), a += 1);
          if (0 === a) throw new Error;
          return i
        }
        return function(e) {
          for (var t = [], s = 0; s < e.length; s += 1) {
            var i = e[s], a = {time: i.tm, duration: i.dr};
            try {
              a.payload = JSON.parse(e[s].cm)
            } catch (t) {
              try {
                a.payload = r(e[s].cm)
              } catch (t) {
                a.payload = {name: e[s]}
              }
            }
            t.push(a)
          }
          return t
        }
      }();
  function Et() {}
  function Mt(t, e) {
    this.animationItem = t, this.layers = null, this.renderedFrame = -1,
    this.svgElement = x('svg');
    var s = '';
    if (e && e.title) {
      var i = x('title'), a = S();
      i.setAttribute('id', a), i.textContent = e.title,
                               this.svgElement.appendChild(i), s += a
    }
    if (e && e.description) {
      var r = x('desc'), n = S();
      r.setAttribute('id', n), r.textContent = e.description,
                               this.svgElement.appendChild(r), s += ' ' + n
    }
    s && this.svgElement.setAttribute('aria-labelledby', s);
    var h = x('defs');
    this.svgElement.appendChild(h);
    var o = x('g');
    this.svgElement.appendChild(o),
        this.layerElement = o, this.renderConfig = {
          preserveAspectRatio: e && e.preserveAspectRatio || 'xMidYMid meet',
          imagePreserveAspectRatio:
              e && e.imagePreserveAspectRatio || 'xMidYMid slice',
          progressiveLoad: e && e.progressiveLoad || !1,
          hideOnTransparent: !(e && !1 === e.hideOnTransparent),
          viewBoxOnly: e && e.viewBoxOnly || !1,
          viewBoxSize: e && e.viewBoxSize || !1,
          className: e && e.className || '',
          id: e && e.id || '',
          focusable: e && e.focusable,
          filterSize: {
            width: e && e.filterSize && e.filterSize.width || '100%',
            height: e && e.filterSize && e.filterSize.height || '100%',
            x: e && e.filterSize && e.filterSize.x || '0%',
            y: e && e.filterSize && e.filterSize.y || '0%'
          }
        },
        this.globalData =
            {_mdf: !1, frameNum: -1, defs: h, renderConfig: this.renderConfig},
        this.elements = [], this.pendingElements = [], this.destroyed = !1,
        this.rendererType = 'svg'
  }
  function It(t, e, s) {
    this.data = t, this.element = e, this.globalData = s, this.storedData = [],
    this.masksProperties = this.data.masksProperties || [],
    this.maskElement = null;
    var i, a, r = this.globalData.defs,
              n = this.masksProperties ? this.masksProperties.length : 0;
    this.viewData = D(n), this.solidPath = '';
    var h, o, l, p, f, d, m = this.masksProperties, c = 0, u = [], g = S(),
                          y = 'clipPath', v = 'clip-path';
    for (i = 0; i < n; i += 1)
      if (('a' !== m[i].mode && 'n' !== m[i].mode || m[i].inv ||
           100 !== m[i].o.k || m[i].o.x) &&
              (v = y = 'mask'),
          's' !== m[i].mode && 'i' !== m[i].mode || 0 !== c ?
              l = null :
              ((l = x('rect')).setAttribute('fill', '#ffffff'),
               l.setAttribute('width', this.element.comp.data.w || 0),
               l.setAttribute('height', this.element.comp.data.h || 0),
               u.push(l)),
          a = x('path'), 'n' === m[i].mode)
        this.viewData[i] = {
          op: R.getProp(this.element, m[i].o, 0, .01, this.element),
          prop: H.getShapeProp(this.element, m[i], 3),
          elem: a,
          lastPath: ''
        },
        r.appendChild(a);
      else {
        var b;
        if (c += 1,
            a.setAttribute('fill', 's' === m[i].mode ? '#000000' : '#ffffff'),
            a.setAttribute('clip-rule', 'nonzero'),
            0 !== m[i].x.k ?
                (v = y = 'mask',
                 d = R.getProp(this.element, m[i].x, 0, null, this.element),
                 b = S(), (p = x('filter')).setAttribute('id', b),
                 (f = x('feMorphology')).setAttribute('operator', 'erode'),
                 f.setAttribute('in', 'SourceGraphic'),
                 f.setAttribute('radius', '0'), p.appendChild(f),
                 r.appendChild(p),
                 a.setAttribute(
                     'stroke', 's' === m[i].mode ? '#000000' : '#ffffff')) :
                d = f = null,
            this.storedData[i] = {
              elem: a,
              x: d,
              expan: f,
              lastPath: '',
              lastOperator: '',
              filterId: b,
              lastRadius: 0
            },
            'i' === m[i].mode) {
          o = u.length;
          var _ = x('g');
          for (h = 0; h < o; h += 1) _.appendChild(u[h]);
          var k = x('mask');
          k.setAttribute('mask-type', 'alpha'),
              k.setAttribute('id', g + '_' + c), k.appendChild(a),
              r.appendChild(k),
              _.setAttribute('mask', 'url(' + A + '#' + g + '_' + c + ')'),
              u.length = 0, u.push(_)
        } else
          u.push(a);
        m[i].inv && !this.solidPath &&
            (this.solidPath = this.createLayerSolidPath()),
            this.viewData[i] = {
              elem: a,
              lastPath: '',
              op: R.getProp(this.element, m[i].o, 0, .01, this.element),
              prop: H.getShapeProp(this.element, m[i], 3),
              invRect: l
            },
            this.viewData[i].prop.k ||
            this.drawPath(m[i], this.viewData[i].prop.v, this.viewData[i])
      }
    for (this.maskElement = x(y), n = u.length, i = 0; i < n; i += 1)
      this.maskElement.appendChild(u[i]);
    0 < c &&
        (this.maskElement.setAttribute('id', g),
         this.element.maskedElement.setAttribute(v, 'url(' + A + '#' + g + ')'),
         r.appendChild(this.maskElement)),
        this.viewData.length && this.element.addRenderableComponent(this)
  }
  function Lt() {}
  function Vt() {}
  function Rt() {}
  function zt() {}
  function Nt() {}
  function Ot(t, e) {
    this.elem = t, this.pos = e
  }
  function qt(t, e) {
    this.data = t, this.type = t.ty, this.d = '', this.lvl = e, this._mdf = !1,
    this.closed = !0 === t.hd, this.pElem = x('path'), this.msElem = null
  }
  function Bt(t, e, s) {
    this.caches = [], this.styles = [], this.transformers = t, this.lStr = '',
    this.sh = s, this.lvl = e, this._isAnimated = !!s.k;
    for (var i = 0, a = t.length; i < a;) {
      if (t[i].mProps.dynamicProperties.length) {
        this._isAnimated = !0;
        break
      }
      i += 1
    }
  }
  function jt(t, e, s) {
    this.transform = {mProps: t, op: e, container: s}, this.elements = [],
    this._isAnimated = this.transform.mProps.dynamicProperties.length ||
        this.transform.op.effectsSequence.length
  }
  function Wt(t, e, s) {
    this.initDynamicPropertyContainer(t),
        this.getValue = this.iterateDynamicProperties,
        this.o = R.getProp(t, e.o, 0, .01, this),
        this.w = R.getProp(t, e.w, 0, null, this),
        this.d = new $(t, e.d || {}, 'svg', this),
        this.c = R.getProp(t, e.c, 1, 255, this), this.style = s,
        this._isAnimated = !!this._isAnimated
  }
  function Xt(t, e, s) {
    this.initDynamicPropertyContainer(t),
        this.getValue = this.iterateDynamicProperties,
        this.o = R.getProp(t, e.o, 0, .01, this),
        this.c = R.getProp(t, e.c, 1, 255, this), this.style = s
  }
  function Ht(t, e, s) {
    this.initDynamicPropertyContainer(t),
        this.getValue = this.iterateDynamicProperties,
        this.initGradientData(t, e, s)
  }
  function Yt(t, e, s) {
    this.initDynamicPropertyContainer(t),
        this.getValue = this.iterateDynamicProperties,
        this.w = R.getProp(t, e.w, 0, null, this),
        this.d = new $(t, e.d || {}, 'svg', this),
        this.initGradientData(t, e, s), this._isAnimated = !!this._isAnimated
  }
  function Gt() {
    this.it = [], this.prevViewData = [], this.gr = x('g')
  }
  Et.prototype.checkLayers =
      function(t) {
    var e, s, i = this.layers.length;
    for (this.completeLayers = !0, e = i - 1; 0 <= e; e -= 1)
      this.elements[e] ||
          (s = this.layers[e]).ip - s.st <= t - this.layers[e].st &&
              s.op - s.st > t - this.layers[e].st && this.buildItem(e),
          this.completeLayers = !!this.elements[e] && this.completeLayers;
    this.checkPendingElements()
  },
  Et.prototype.createItem =
      function(t) {
    switch (t.ty) {
      case 2:
        return this.createImage(t);
      case 0:
        return this.createComp(t);
      case 1:
        return this.createSolid(t);
      case 3:
        return this.createNull(t);
      case 4:
        return this.createShape(t);
      case 5:
        return this.createText(t);
      case 6:
        return this.createAudio(t);
      case 13:
        return this.createCamera(t);
      case 15:
        return this.createFootage(t);
      default:
        return this.createNull(t)
    }
  },
  Et.prototype.createCamera =
      function() {
    throw new Error('You\'re using a 3d camera. Try the html renderer.')
  },
  Et.prototype.createAudio =
      function(t) {
    return new ie(t, this.globalData, this)
  },
  Et.prototype.createFootage =
      function(t) {
    return new FootageElement(t, this.globalData, this)
  },
  Et.prototype.buildAllItems =
      function() {
    var t, e = this.layers.length;
    for (t = 0; t < e; t += 1) this.buildItem(t);
    this.checkPendingElements()
  },
  Et.prototype.includeLayers =
      function(t) {
    var e;
    this.completeLayers = !1;
    var s, i = t.length, a = this.layers.length;
    for (e = 0; e < i; e += 1)
      for (s = 0; s < a;) {
        if (this.layers[s].id === t[e].id) {
          this.layers[s] = t[e];
          break
        }
        s += 1
      }
  },
  Et.prototype.setProjectInterface =
      function(t) {
    this.globalData.projectInterface = t
  },
  Et.prototype.initItems =
      function() {
    this.globalData.progressiveLoad || this.buildAllItems()
  },
  Et.prototype.buildElementParenting =
      function(t, e, s) {
    for (var i = this.elements, a = this.layers, r = 0, n = a.length; r < n;)
      a[r].ind == e &&
          (i[r] && !0 !== i[r] ?
               (s.push(i[r]), i[r].setAsParent(),
                void 0 !== a[r].parent ?
                    this.buildElementParenting(t, a[r].parent, s) :
                    t.setHierarchy(s)) :
               (this.buildItem(r), this.addPendingElement(t))),
          r += 1
  },
  Et.prototype.addPendingElement =
      function(t) {
    this.pendingElements.push(t)
  },
  Et.prototype.searchExtraCompositions =
      function(t) {
    var e, s = t.length;
    for (e = 0; e < s; e += 1)
      if (t[e].xt) {
        var i = this.createComp(t[e]);
        i.initExpressions(),
            this.globalData.projectInterface.registerComposition(i)
      }
  },
  Et.prototype.setupGlobalData =
      function(t, e) {
    this.globalData.fontManager = new V,
    this.globalData.fontManager.addChars(t.chars),
    this.globalData.fontManager.addFonts(t.fonts, e),
    this.globalData.getAssetData =
        this.animationItem.getAssetData.bind(this.animationItem),
    this.globalData.getAssetsPath =
        this.animationItem.getAssetsPath.bind(this.animationItem),
    this.globalData.imageLoader = this.animationItem.imagePreloader,
    this.globalData.audioController = this.animationItem.audioController,
    this.globalData.frameId = 0, this.globalData.frameRate = t.fr,
    this.globalData.nm = t.nm, this.globalData.compSize = {w: t.w, h: t.h}
  },
  M([Et], Mt),
  Mt.prototype.createNull =
      function(t) {
    return new Ut(t, this.globalData, this)
  },
  Mt.prototype.createShape =
      function(t) {
    return new ne(t, this.globalData, this)
  },
  Mt.prototype.createText =
      function(t) {
    return new re(t, this.globalData, this)
  },
  Mt.prototype.createImage =
      function(t) {
    return new ee(t, this.globalData, this)
  },
  Mt.prototype.createComp =
      function(t) {
    return new ae(t, this.globalData, this)
  },
  Mt.prototype.createSolid =
      function(t) {
    return new se(t, this.globalData, this)
  },
  Mt.prototype.configAnimation =
      function(t) {
    this.svgElement.setAttribute('xmlns', 'http://www.w3.org/2000/svg'),
        this.renderConfig.viewBoxSize ?
        this.svgElement.setAttribute('viewBox', this.renderConfig.viewBoxSize) :
        this.svgElement.setAttribute('viewBox', '0 0 ' + t.w + ' ' + t.h),
        this.renderConfig.viewBoxOnly ||
        (this.svgElement.setAttribute('width', t.w),
         this.svgElement.setAttribute('height', t.h),
         this.svgElement.style.width = '100%',
         this.svgElement.style.height = '100%',
         this.svgElement.style.transform = 'translate3d(0,0,0)'),
        this.renderConfig.className &&
        this.svgElement.setAttribute('class', this.renderConfig.className),
        this.renderConfig.id &&
        this.svgElement.setAttribute('id', this.renderConfig.id),
        void 0 !== this.renderConfig.focusable &&
        this.svgElement.setAttribute('focusable', this.renderConfig.focusable),
        this.svgElement.setAttribute(
            'preserveAspectRatio', this.renderConfig.preserveAspectRatio),
        this.animationItem.wrapper.appendChild(this.svgElement);
    var e = this.globalData.defs;
    this.setupGlobalData(t, e),
        this.globalData.progressiveLoad = this.renderConfig.progressiveLoad,
        this.data = t;
    var s = x('clipPath'), i = x('rect');
    i.setAttribute('width', t.w), i.setAttribute('height', t.h),
        i.setAttribute('x', 0), i.setAttribute('y', 0);
    var a = S();
    s.setAttribute('id', a), s.appendChild(i),
        this.layerElement.setAttribute('clip-path', 'url(' + A + '#' + a + ')'),
        e.appendChild(s), this.layers = t.layers,
                          this.elements = D(t.layers.length)
  },
  Mt.prototype.destroy =
      function() {
    var t;
    this.animationItem.wrapper && (this.animationItem.wrapper.innerText = ''),
        this.layerElement = null, this.globalData.defs = null;
    var e = this.layers ? this.layers.length : 0;
    for (t = 0; t < e; t += 1) this.elements[t] && this.elements[t].destroy();
    this.elements.length = 0, this.destroyed = !0, this.animationItem = null
  },
  Mt.prototype.updateContainerSize = function() {},
  Mt.prototype.buildItem =
      function(t) {
    var e = this.elements;
    if (!e[t] && 99 !== this.layers[t].ty) {
      e[t] = !0;
      var s = this.createItem(this.layers[t]);
      e[t] = s,
      h &&
          (0 === this.layers[t].ty &&
               this.globalData.projectInterface.registerComposition(s),
           s.initExpressions()),
      this.appendElementInPos(s, t),
      this.layers[t].tt &&
          (this.elements[t - 1] && !0 !== this.elements[t - 1] ?
               s.setMatte(e[t - 1].layerId) :
               (this.buildItem(t - 1), this.addPendingElement(s)))
    }
  },
  Mt.prototype.checkPendingElements =
      function() {
    for (; this.pendingElements.length;) {
      var t = this.pendingElements.pop();
      if (t.checkParenting(), t.data.tt)
        for (var e = 0, s = this.elements.length; e < s;) {
          if (this.elements[e] === t) {
            t.setMatte(this.elements[e - 1].layerId);
            break
          }
          e += 1
        }
    }
  },
  Mt.prototype.renderFrame =
      function(t) {
    if (this.renderedFrame !== t && !this.destroyed) {
      var e;
      null === t ? t = this.renderedFrame : this.renderedFrame = t,
                   this.globalData.frameNum = t, this.globalData.frameId += 1,
                   this.globalData.projectInterface.currentFrame = t,
                   this.globalData._mdf = !1;
      var s = this.layers.length;
      for (this.completeLayers || this.checkLayers(t), e = s - 1; 0 <= e;
           e -= 1)
        (this.completeLayers || this.elements[e]) &&
            this.elements[e].prepareFrame(t - this.layers[e].st);
      if (this.globalData._mdf)
        for (e = 0; e < s; e += 1)
          (this.completeLayers || this.elements[e]) &&
              this.elements[e].renderFrame()
    }
  },
  Mt.prototype.appendElementInPos =
      function(t, e) {
    var s = t.getBaseElement();
    if (s) {
      for (var i, a = 0; a < e;)
        this.elements[a] && !0 !== this.elements[a] &&
            this.elements[a].getBaseElement() &&
            (i = this.elements[a].getBaseElement()),
            a += 1;
      i ? this.layerElement.insertBefore(s, i) :
          this.layerElement.appendChild(s)
    }
  },
  Mt.prototype.hide =
      function() {
    this.layerElement.style.display = 'none'
  },
  Mt.prototype.show =
      function() {
    this.layerElement.style.display = 'block'
  },
  It.prototype.getMaskProperty =
      function(t) {
    return this.viewData[t].prop
  },
  It.prototype.renderFrame =
      function(t) {
    var e, s = this.element.finalTransform.mat, i = this.masksProperties.length;
    for (e = 0; e < i; e += 1)
      if ((this.viewData[e].prop._mdf || t) &&
              this.drawPath(
                  this.masksProperties[e], this.viewData[e].prop.v,
                  this.viewData[e]),
          (this.viewData[e].op._mdf || t) &&
              this.viewData[e].elem.setAttribute(
                  'fill-opacity', this.viewData[e].op.v),
          'n' !== this.masksProperties[e].mode &&
              (this.viewData[e].invRect &&
                   (this.element.finalTransform.mProp._mdf || t) &&
                   this.viewData[e].invRect.setAttribute(
                       'transform', s.getInverseMatrix().to2dCSS()),
               this.storedData[e].x && (this.storedData[e].x._mdf || t))) {
        var a = this.storedData[e].expan;
        this.storedData[e].x.v < 0 ?
            ('erode' !== this.storedData[e].lastOperator &&
                 (this.storedData[e].lastOperator = 'erode',
                  this.storedData[e].elem.setAttribute(
                      'filter',
                      'url(' + A + '#' + this.storedData[e].filterId + ')')),
             a.setAttribute('radius', -this.storedData[e].x.v)) :
            ('dilate' !== this.storedData[e].lastOperator &&
                 (this.storedData[e].lastOperator = 'dilate',
                  this.storedData[e].elem.setAttribute('filter', null)),
             this.storedData[e].elem.setAttribute(
                 'stroke-width', 2 * this.storedData[e].x.v))
      }
  },
  It.prototype.getMaskelement =
      function() {
    return this.maskElement
  },
  It.prototype.createLayerSolidPath =
      function() {
    var t = 'M0,0 ';
    return t += ' h' + this.globalData.compSize.w,
           t += ' v' + this.globalData.compSize.h,
           t += ' h-' + this.globalData.compSize.w,
           t += ' v-' + this.globalData.compSize.h + ' '
  },
  It.prototype.drawPath =
      function(t, e, s) {
    var i, a, r = ' M' + e.v[0][0] + ',' + e.v[0][1];
    for (a = e._length, i = 1; i < a; i += 1)
      r += ' C' + e.o[i - 1][0] + ',' + e.o[i - 1][1] + ' ' + e.i[i][0] + ',' +
          e.i[i][1] + ' ' + e.v[i][0] + ',' + e.v[i][1];
    if (e.c && 1 < a &&
            (r += ' C' + e.o[i - 1][0] + ',' + e.o[i - 1][1] + ' ' + e.i[0][0] +
                 ',' + e.i[0][1] + ' ' + e.v[0][0] + ',' + e.v[0][1]),
        s.lastPath !== r) {
      var n = '';
      s.elem &&
          (e.c && (n = t.inv ? this.solidPath + r : r),
           s.elem.setAttribute('d', n)),
          s.lastPath = r
    }
  },
  It.prototype.destroy =
      function() {
    this.element = null, this.globalData = null, this.maskElement = null,
    this.data = null, this.masksProperties = null
  },
  Lt.prototype = {
    initHierarchy: function() {
      this.hierarchy = [], this._isParent = !1, this.checkParenting()
    },
    setHierarchy: function(t) {
      this.hierarchy = t
    },
    setAsParent: function() {
      this._isParent = !0
    },
    checkParenting: function() {
      void 0 !== this.data.parent &&
          this.comp.buildElementParenting(this, this.data.parent, [])
    }
  },
  Vt.prototype = {
    initFrame: function() {
      this._isFirstFrame = !1, this.dynamicProperties = [], this._mdf = !1
    },
    prepareProperties: function(t, e) {
      var s, i = this.dynamicProperties.length;
      for (s = 0; s < i; s += 1)
        (e ||
         this._isParent &&
             'transform' === this.dynamicProperties[s].propType) &&
            (this.dynamicProperties[s].getValue(),
             this.dynamicProperties[s]._mdf &&
                 (this.globalData._mdf = !0, this._mdf = !0))
    },
    addDynamicProperty: function(t) {
      -1 === this.dynamicProperties.indexOf(t) && this.dynamicProperties.push(t)
    }
  },
  Rt.prototype = {
    initTransform: function() {
      this.finalTransform = {
        mProp: this.data.ks ? z.getTransformProperty(this, this.data.ks, this) :
                              {o: 0},
        _matMdf: !1,
        _opMdf: !1,
        mat: new I
      },
      this.data.ao && (this.finalTransform.mProp.autoOriented = !0),
      this.data.ty
    },
    renderTransform: function() {
      if (this.finalTransform._opMdf =
              this.finalTransform.mProp.o._mdf || this._isFirstFrame,
          this.finalTransform._matMdf =
              this.finalTransform.mProp._mdf || this._isFirstFrame,
          this.hierarchy) {
        var t, e = this.finalTransform.mat, s = 0, i = this.hierarchy.length;
        if (!this.finalTransform._matMdf)
          for (; s < i;) {
            if (this.hierarchy[s].finalTransform.mProp._mdf) {
              this.finalTransform._matMdf = !0;
              break
            }
            s += 1
          }
        if (this.finalTransform._matMdf)
          for (t = this.finalTransform.mProp.v.props, e.cloneFromProps(t),
              s = 0;
               s < i; s += 1)
            t = this.hierarchy[s].finalTransform.mProp.v.props,
            e.transform(
                t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9],
                t[10], t[11], t[12], t[13], t[14], t[15])
      }
    },
    globalToLocal: function(t) {
      var e = [];
      e.push(this.finalTransform);
      for (var s, i = !0, a = this.comp; i;)
        a.finalTransform ?
            (a.data.hasMask && e.splice(0, 0, a.finalTransform), a = a.comp) :
            i = !1;
      var r, n = e.length;
      for (s = 0; s < n; s += 1)
        r = e[s].mat.applyToPointArray(0, 0, 0),
        t = [t[0] - r[0], t[1] - r[1], 0];
      return t
    },
    mHelper: new I
  },
  zt.prototype = {
    initRenderable: function() {
      this.isInRange = !1, this.hidden = !1, this.isTransparent = !1,
      this.renderableComponents = []
    },
    addRenderableComponent: function(t) {
      -1 === this.renderableComponents.indexOf(t) &&
          this.renderableComponents.push(t)
    },
    removeRenderableComponent: function(t) {
      -1 !== this.renderableComponents.indexOf(t) &&
          this.renderableComponents.splice(
              this.renderableComponents.indexOf(t), 1)
    },
    prepareRenderableFrame: function(t) {
      this.checkLayerLimits(t)
    },
    checkTransparency: function() {
      this.finalTransform.mProp.o.v <= 0 ?
          !this.isTransparent &&
              this.globalData.renderConfig.hideOnTransparent &&
              (this.isTransparent = !0, this.hide()) :
          this.isTransparent && (this.isTransparent = !1, this.show())
    },
    checkLayerLimits: function(t) {
      this.data.ip - this.data.st <= t && this.data.op - this.data.st > t ?
          !0 !== this.isInRange &&
              (this.globalData._mdf = !0, this._mdf = !0, this.isInRange = !0,
               this.show()) :
          !1 !== this.isInRange &&
              (this.globalData._mdf = !0, this.isInRange = !1, this.hide())
    },
    renderRenderable: function() {
      var t, e = this.renderableComponents.length;
      for (t = 0; t < e; t += 1)
        this.renderableComponents[t].renderFrame(this._isFirstFrame)
    },
    sourceRectAtTime: function() {
      return {
        top: 0, left: 0, width: 100, height: 100
      }
    },
    getLayerSize: function() {
      return 5 === this.data.ty ?
          {w: this.data.textData.width, h: this.data.textData.height} :
          {w: this.data.width, h: this.data.height}
    }
  },
  M(
      [
        zt,
        function(t) {
          function e() {}
          return e.prototype = t, e
        }({
          initElement: function(t, e, s) {
            this.initFrame(), this.initBaseData(t, e, s),
                this.initTransform(t, e, s), this.initHierarchy(),
                this.initRenderable(), this.initRendererElement(),
                this.createContainerElements(),
                this.createRenderableComponents(), this.createContent(),
                this.hide()
          },
          hide: function() {
            this.hidden || this.isInRange && !this.isTransparent ||
                ((this.baseElement || this.layerElement).style.display = 'none',
                 this.hidden = !0)
          },
          show: function() {
            this.isInRange && !this.isTransparent &&
                (this.data.hd ||
                     ((this.baseElement || this.layerElement).style.display =
                          'block'),
                 this.hidden = !1, this._isFirstFrame = !0)
          },
          renderFrame: function() {
            this.data.hd || this.hidden ||
                (this.renderTransform(), this.renderRenderable(),
                 this.renderElement(), this.renderInnerContent(),
                 this._isFirstFrame && (this._isFirstFrame = !1))
          },
          renderInnerContent: function() {},
          prepareFrame: function(t) {
            this._mdf = !1, this.prepareRenderableFrame(t),
            this.prepareProperties(t, this.isInRange), this.checkTransparency()
          },
          destroy: function() {
            this.innerElem = null, this.destroyBaseElement()
          }
        })
      ],
      Nt),
  qt.prototype.reset = function() {
    this.d = '', this._mdf = !1
  }, Bt.prototype.setAsAnimated = function() {
    this._isAnimated = !0
  }, M([F], Wt), M([F], Xt), Ht.prototype.initGradientData = function(t, e, s) {
    this.o = R.getProp(t, e.o, 0, .01, this),
    this.s = R.getProp(t, e.s, 1, null, this),
    this.e = R.getProp(t, e.e, 1, null, this),
    this.h = R.getProp(t, e.h || {k: 0}, 0, .01, this),
    this.a = R.getProp(t, e.a || {k: 0}, 0, B, this),
    this.g = new tt(t, e.g, this), this.style = s, this.stops = [],
    this.setGradientData(s.pElem, e), this.setGradientOpacity(e, s),
    this._isAnimated = !!this._isAnimated
  }, Ht.prototype.setGradientData = function(t, e) {
    var s = S(), i = x(1 === e.t ? 'linearGradient' : 'radialGradient');
    i.setAttribute('id', s), i.setAttribute('spreadMethod', 'pad'),
        i.setAttribute('gradientUnits', 'userSpaceOnUse');
    var a, r, n, h = [];
    for (n = 4 * e.g.p, r = 0; r < n; r += 4)
      a = x('stop'), i.appendChild(a), h.push(a);
    t.setAttribute(
        'gf' === e.ty ? 'fill' : 'stroke', 'url(' + A + '#' + s + ')'),
        this.gf = i, this.cst = h
  }, Ht.prototype.setGradientOpacity = function(t, e) {
    if (this.g._hasOpacity && !this.g._collapsable) {
      var s, i, a, r = x('mask'), n = x('path');
      r.appendChild(n);
      var h = S(), o = S();
      r.setAttribute('id', o);
      var l = x(1 === t.t ? 'linearGradient' : 'radialGradient');
      l.setAttribute('id', h), l.setAttribute('spreadMethod', 'pad'),
          l.setAttribute('gradientUnits', 'userSpaceOnUse'),
          a = t.g.k.k[0].s ? t.g.k.k[0].s.length : t.g.k.k.length;
      var p = this.stops;
      for (i = 4 * t.g.p; i < a; i += 2)
        (s = x('stop')).setAttribute('stop-color', 'rgb(255,255,255)'),
            l.appendChild(s), p.push(s);
      n.setAttribute(
          'gf' === t.ty ? 'fill' : 'stroke', 'url(' + A + '#' + h + ')'),
          this.of = l, this.ms = r, this.ost = p, this.maskId = o, e.msElem = n
    }
  }, M([F], Ht), M([Ht, F], Yt);
  var Kt = function() {
    var g = new I, y = new I;
    function e(t, e, s) {
      (s || e.transform.op._mdf) &&
          e.transform.container.setAttribute('opacity', e.transform.op.v),
          (s || e.transform.mProps._mdf) &&
          e.transform.container.setAttribute(
              'transform', e.transform.mProps.v.to2dCSS())
    }
    function s(t, e, s) {
      var i, a, r, n, h, o, l, p, f, d, m, c = e.styles.length, u = e.lvl;
      for (o = 0; o < c; o += 1) {
        if (n = e.sh._mdf || s, e.styles[o].lvl < u) {
          for (p = y.reset(), d = u - e.styles[o].lvl,
              m = e.transformers.length - 1;
               !n && 0 < d;)
            n = e.transformers[m].mProps._mdf || n, d -= 1, m -= 1;
          if (n)
            for (d = u - e.styles[o].lvl, m = e.transformers.length - 1; 0 < d;)
              f = e.transformers[m].mProps.v.props,
              p.transform(
                  f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9],
                  f[10], f[11], f[12], f[13], f[14], f[15]),
              d -= 1, m -= 1
        } else
          p = g;
        if (a = (l = e.sh.paths)._length, n) {
          for (r = '', i = 0; i < a; i += 1)
            (h = l.shapes[i]) && h._length && (r += it(h, h._length, h.c, p));
          e.caches[o] = r
        } else
          r = e.caches[o];
        e.styles[o].d += !0 === t.hd ? '' : r,
            e.styles[o]._mdf = n || e.styles[o]._mdf
      }
    }
    function i(t, e, s) {
      var i = e.style;
      (e.c._mdf || s) &&
          i.pElem.setAttribute(
              'fill',
              'rgb(' + f(e.c.v[0]) + ',' + f(e.c.v[1]) + ',' + f(e.c.v[2]) +
                  ')'),
          (e.o._mdf || s) && i.pElem.setAttribute('fill-opacity', e.o.v)
    }
    function a(t, e, s) {
      r(t, e, s), n(t, e, s)
    }
    function r(t, e, s) {
      var i, a, r, n, h, o = e.gf, l = e.g._hasOpacity, p = e.s.v, f = e.e.v;
      if (e.o._mdf || s) {
        var d = 'gf' === t.ty ? 'fill-opacity' : 'stroke-opacity';
        e.style.pElem.setAttribute(d, e.o.v)
      }
      if (e.s._mdf || s) {
        var m = 1 === t.t ? 'x1' : 'cx', c = 'x1' === m ? 'y1' : 'cy';
        o.setAttribute(m, p[0]), o.setAttribute(c, p[1]),
            l && !e.g._collapsable &&
            (e.of.setAttribute(m, p[0]), e.of.setAttribute(c, p[1]))
      }
      if (e.g._cmdf || s) {
        i = e.cst;
        var u = e.g.c;
        for (r = i.length, a = 0; a < r; a += 1)
          (n = i[a]).setAttribute('offset', u[4 * a] + '%'),
              n.setAttribute(
                  'stop-color',
                  'rgb(' + u[4 * a + 1] + ',' + u[4 * a + 2] + ',' +
                      u[4 * a + 3] + ')')
      }
      if (l && (e.g._omdf || s)) {
        var g = e.g.o;
        for (r = (i = e.g._collapsable ? e.cst : e.ost).length, a = 0; a < r;
             a += 1)
          n = i[a],
          e.g._collapsable || n.setAttribute('offset', g[2 * a] + '%'),
          n.setAttribute('stop-opacity', g[2 * a + 1])
      }
      if (1 === t.t)
        (e.e._mdf || s) &&
            (o.setAttribute('x2', f[0]), o.setAttribute('y2', f[1]),
             l && !e.g._collapsable &&
                 (e.of.setAttribute('x2', f[0]),
                  e.of.setAttribute('y2', f[1])));
      else if (
          (e.s._mdf || e.e._mdf || s) &&
              (h = Math.sqrt(
                   Math.pow(p[0] - f[0], 2) + Math.pow(p[1] - f[1], 2)),
               o.setAttribute('r', h),
               l && !e.g._collapsable && e.of.setAttribute('r', h)),
          e.e._mdf || e.h._mdf || e.a._mdf || s) {
        h ||
            (h = Math.sqrt(
                 Math.pow(p[0] - f[0], 2) + Math.pow(p[1] - f[1], 2)));
        var y = Math.atan2(f[1] - p[1], f[0] - p[0]), v = e.h.v;
        1 <= v ? v = .99 : v <= -1 && (v = -.99);
        var b = h * v, _ = Math.cos(y + e.a.v) * b + p[0],
            k = Math.sin(y + e.a.v) * b + p[1];
        o.setAttribute('fx', _), o.setAttribute('fy', k),
            l && !e.g._collapsable &&
            (e.of.setAttribute('fx', _), e.of.setAttribute('fy', k))
      }
    }
    function n(t, e, s) {
      var i = e.style, a = e.d;
      a && (a._mdf || s) && a.dashStr &&
          (i.pElem.setAttribute('stroke-dasharray', a.dashStr),
           i.pElem.setAttribute('stroke-dashoffset', a.dashoffset[0])),
          e.c && (e.c._mdf || s) &&
          i.pElem.setAttribute(
              'stroke',
              'rgb(' + f(e.c.v[0]) + ',' + f(e.c.v[1]) + ',' + f(e.c.v[2]) +
                  ')'),
          (e.o._mdf || s) && i.pElem.setAttribute('stroke-opacity', e.o.v),
          (e.w._mdf || s) &&
          (i.pElem.setAttribute('stroke-width', e.w.v),
           i.msElem && i.msElem.setAttribute('stroke-width', e.w.v))
    }
    return {
      createRenderFunction: function(t) {
        switch (t.ty) {
          case 'fl':
            return i;
          case 'gf':
            return r;
          case 'gs':
            return a;
          case 'st':
            return n;
          case 'sh':
          case 'el':
          case 'rc':
          case 'sr':
            return s;
          case 'tr':
            return e;
          default:
            return null
        }
      }
    }
  }();
  function Jt() {}
  function Ut(t, e, s) {
    this.initFrame(), this.initBaseData(t, e, s), this.initFrame(),
        this.initTransform(t, e, s), this.initHierarchy()
  }
  function Zt() {}
  function Qt() {}
  function $t() {}
  function te() {}
  function ee(t, e, s) {
    this.assetData = e.getAssetData(t.refId), this.initElement(t, e, s),
    this.sourceRect = {
      top: 0,
      left: 0,
      width: this.assetData.w,
      height: this.assetData.h
    }
  }
  function se(t, e, s) {
    this.initElement(t, e, s)
  }
  function ie(t, e, s) {
    this.initFrame(), this.initRenderable(),
        this.assetData = e.getAssetData(t.refId), this.initBaseData(t, e, s),
        this._isPlaying = !1, this._canPlay = !1;
    var i = this.globalData.getAssetsPath(this.assetData);
    this.audio = this.globalData.audioController.createAudio(i),
    this._currentTime = 0, this.globalData.audioController.addAudio(this),
    this.tm =
        t.tm ? R.getProp(this, t.tm, 0, e.frameRate, this) : {_placeholder: !0}
  }
  function ae(t, e, s) {
    this.layers = t.layers, this.supports3d = !0, this.completeLayers = !1,
    this.pendingElements = [],
    this.elements = this.layers ? D(this.layers.length) : [],
    this.initElement(t, e, s),
    this.tm =
        t.tm ? R.getProp(this, t.tm, 0, e.frameRate, this) : {_placeholder: !0}
  }
  function re(t, e, s) {
    this.textSpans = [], this.renderType = 'svg', this.initElement(t, e, s)
  }
  function ne(t, e, s) {
    this.shapes = [], this.shapesData = t.shapes, this.stylesList = [],
    this.shapeModifiers = [], this.itemsData = [], this.processedElements = [],
    this.animatedContents = [], this.initElement(t, e, s),
    this.prevViewData = []
  }
  Jt.prototype = {
    checkMasks: function() {
      if (!this.data.hasMask) return !1;
      for (var t = 0, e = this.data.masksProperties.length; t < e;) {
        if ('n' !== this.data.masksProperties[t].mode &&
            !1 !== this.data.masksProperties[t].cl)
          return !0;
        t += 1
      }
      return !1
    },
    initExpressions: function() {
      this.layerInterface = LayerExpressionInterface(this),
      this.data.hasMask && this.maskManager &&
          this.layerInterface.registerMaskInterface(this.maskManager);
      var t = EffectsExpressionInterface.createEffectsInterface(
          this, this.layerInterface);
      this.layerInterface.registerEffectsInterface(t),
          0 === this.data.ty || this.data.xt ?
          this.compInterface = CompExpressionInterface(this) :
          4 === this.data.ty ?
          (this.layerInterface.shapeInterface = ShapeExpressionInterface(
               this.shapesData, this.itemsData, this.layerInterface),
           this.layerInterface.content = this.layerInterface.shapeInterface) :
          5 === this.data.ty &&
              (this.layerInterface.textInterface =
                   TextExpressionInterface(this),
               this.layerInterface.text = this.layerInterface.textInterface)
    },
    setBlendMode: function() {
      var t = E(this.data.bm);
      (this.baseElement || this.layerElement).style['mix-blend-mode'] = t
    },
    initBaseData: function(t, e, s) {
      this.globalData = e, this.comp = s, this.data = t, this.layerId = S(),
      this.data.sr || (this.data.sr = 1),
      this.effectsManager = new fe(this.data, this, this.dynamicProperties)
    },
    getType: function() {
      return this.type
    },
    sourceRectAtTime: function() {}
  },
  Ut.prototype.prepareFrame =
      function(t) {
    this.prepareProperties(t, !0)
  },
  Ut.prototype.renderFrame = function() {},
  Ut.prototype.getBaseElement =
      function() {
    return null
  },
  Ut.prototype.destroy = function() {},
  Ut.prototype.sourceRectAtTime = function() {},
  Ut.prototype.hide = function() {}, M([Jt, Rt, Lt, Vt], Ut), Zt.prototype = {
    initRendererElement: function() {
      this.layerElement = x('g')
    },
    createContainerElements: function() {
      this.matteElement = x('g'), this.transformedElement = this.layerElement,
      this.maskedElement = this.layerElement, this._sizeChanged = !1;
      var t, e, s, i = null;
      if (this.data.td) {
        if (3 == this.data.td || 1 == this.data.td) {
          var a = x('mask');
          a.setAttribute('id', this.layerId),
              a.setAttribute(
                  'mask-type', 3 == this.data.td ? 'luminance' : 'alpha'),
              a.appendChild(this.layerElement),
              i = a, this.globalData.defs.appendChild(a),
              nt.maskType || 1 != this.data.td ||
              (a.setAttribute('mask-type', 'luminance'), t = S(),
               e = ht.createFilter(t), this.globalData.defs.appendChild(e),
               e.appendChild(ht.createAlphaToLuminanceFilter()),
               (s = x('g')).appendChild(this.layerElement), i = s,
               a.appendChild(s),
               s.setAttribute('filter', 'url(' + A + '#' + t + ')'))
        } else if (2 == this.data.td) {
          var r = x('mask');
          r.setAttribute('id', this.layerId),
              r.setAttribute('mask-type', 'alpha');
          var n = x('g');
          r.appendChild(n), t = S(), e = ht.createFilter(t);
          var h = x('feComponentTransfer');
          h.setAttribute('in', 'SourceGraphic'), e.appendChild(h);
          var o = x('feFuncA');
          o.setAttribute('type', 'table'),
              o.setAttribute('tableValues', '1.0 0.0'), h.appendChild(o),
              this.globalData.defs.appendChild(e);
          var l = x('rect');
          l.setAttribute('width', this.comp.data.w),
              l.setAttribute('height', this.comp.data.h),
              l.setAttribute('x', '0'), l.setAttribute('y', '0'),
              l.setAttribute('fill', '#ffffff'), l.setAttribute('opacity', '0'),
              n.setAttribute('filter', 'url(' + A + '#' + t + ')'),
              n.appendChild(l), n.appendChild(this.layerElement),
              i = n,
              nt.maskType ||
              (r.setAttribute('mask-type', 'luminance'),
               e.appendChild(ht.createAlphaToLuminanceFilter()), s = x('g'),
               n.appendChild(l), s.appendChild(this.layerElement), i = s,
               n.appendChild(s)),
              this.globalData.defs.appendChild(r)
        }
      } else
        this.data.tt ?
            (this.matteElement.appendChild(this.layerElement),
             i = this.matteElement, this.baseElement = this.matteElement) :
            this.baseElement = this.layerElement;
      if (this.data.ln && this.layerElement.setAttribute('id', this.data.ln),
          this.data.cl && this.layerElement.setAttribute('class', this.data.cl),
          0 === this.data.ty && !this.data.hd) {
        var p = x('clipPath'), f = x('path');
        f.setAttribute(
            'd',
            'M0,0 L' + this.data.w + ',0 L' + this.data.w + ',' + this.data.h +
                ' L0,' + this.data.h + 'z');
        var d = S();
        if (p.setAttribute('id', d), p.appendChild(f),
            this.globalData.defs.appendChild(p), this.checkMasks()) {
          var m = x('g');
          m.setAttribute('clip-path', 'url(' + A + '#' + d + ')'),
              m.appendChild(this.layerElement),
              this.transformedElement = m,
              i ? i.appendChild(this.transformedElement) :
                  this.baseElement = this.transformedElement
        } else
          this.layerElement.setAttribute(
              'clip-path', 'url(' + A + '#' + d + ')')
      }
      0 !== this.data.bm && this.setBlendMode()
    },
    renderElement: function() {
      this.finalTransform._matMdf &&
          this.transformedElement.setAttribute(
              'transform', this.finalTransform.mat.to2dCSS()),
          this.finalTransform._opMdf &&
          this.transformedElement.setAttribute(
              'opacity', this.finalTransform.mProp.o.v)
    },
    destroyBaseElement: function() {
      this.layerElement = null, this.matteElement = null,
      this.maskManager.destroy()
    },
    getBaseElement: function() {
      return this.data.hd ? null : this.baseElement
    },
    createRenderableComponents: function() {
      this.maskManager = new It(this.data, this, this.globalData),
      this.renderableEffectsManager = new oe(this)
    },
    setMatte: function(t) {
      this.matteElement &&
          this.matteElement.setAttribute('mask', 'url(' + A + '#' + t + ')')
    }
  },
  Qt.prototype = {
    addShapeToModifiers: function(t) {
      var e, s = this.shapeModifiers.length;
      for (e = 0; e < s; e += 1) this.shapeModifiers[e].addShape(t)
    },
    isShapeInAnimatedModifiers: function(t) {
      for (var e = this.shapeModifiers.length; 0 < e;)
        if (this.shapeModifiers[0].isAnimatedWithShape(t)) return !0;
      return !1
    },
    renderModifiers: function() {
      if (this.shapeModifiers.length) {
        var t, e = this.shapes.length;
        for (t = 0; t < e; t += 1) this.shapes[t].sh.reset();
        for (t = (e = this.shapeModifiers.length) - 1; 0 <= t &&
             !this.shapeModifiers[t].processShapes(this._isFirstFrame);
             t -= 1);
      }
    },
    lcEnum: {1: 'butt', 2: 'round', 3: 'square'},
    ljEnum: {1: 'miter', 2: 'round', 3: 'bevel'},
    searchProcessedElement: function(t) {
      for (var e = this.processedElements, s = 0, i = e.length; s < i;) {
        if (e[s].elem === t) return e[s].pos;
        s += 1
      }
      return 0
    },
    addProcessedElement: function(t, e) {
      for (var s = this.processedElements, i = s.length; i;)
        if (s[i -= 1].elem === t) return void (s[i].pos = e);
      s.push(new Ot(t, e))
    },
    prepareFrame: function(t) {
      this.prepareRenderableFrame(t), this.prepareProperties(t, this.isInRange)
    }
  },
  $t.prototype.initElement =
      function(t, e, s) {
    this.lettersChangedFlag = !0, this.initFrame(), this.initBaseData(t, e, s),
    this.textProperty = new gt(this, t.t, this.dynamicProperties),
    this.textAnimator = new mt(t.t, this.renderType, this),
    this.initTransform(t, e, s), this.initHierarchy(), this.initRenderable(),
    this.initRendererElement(), this.createContainerElements(),
    this.createRenderableComponents(), this.createContent(), this.hide(),
    this.textAnimator.searchProperties(this.dynamicProperties)
  },
  $t.prototype.prepareFrame =
      function(t) {
    this._mdf = !1, this.prepareRenderableFrame(t),
    this.prepareProperties(t, this.isInRange),
    (this.textProperty._mdf || this.textProperty._isFirstFrame) &&
        (this.buildNewText(), this.textProperty._isFirstFrame = !1,
         this.textProperty._mdf = !1)
  },
  $t.prototype.createPathShape =
      function(t, e) {
    var s, i, a = e.length, r = '';
    for (s = 0; s < a; s += 1) i = e[s].ks.k, r += it(i, i.i.length, !0, t);
    return r
  },
  $t.prototype.updateDocumentData =
      function(t, e) {
    this.textProperty.updateDocumentData(t, e)
  },
  $t.prototype.canResizeFont =
      function(t) {
    this.textProperty.canResizeFont(t)
  },
  $t.prototype.setMinimumFontSize =
      function(t) {
    this.textProperty.setMinimumFontSize(t)
  },
  $t.prototype.applyTextPropertiesToMatrix =
      function(t, e, s, i, a) {
    switch (t.ps && e.translate(t.ps[0], t.ps[1] + t.ascent, 0),
            e.translate(0, -t.ls, 0), t.j) {
      case 1:
        e.translate(t.justifyOffset + (t.boxWidth - t.lineWidths[s]), 0, 0);
        break;
      case 2:
        e.translate(t.justifyOffset + (t.boxWidth - t.lineWidths[s]) / 2, 0, 0)
    }
    e.translate(i, a, 0)
  },
  $t.prototype.buildColor =
      function(t) {
    return 'rgb(' + Math.round(255 * t[0]) + ',' + Math.round(255 * t[1]) +
        ',' + Math.round(255 * t[2]) + ')'
  },
  $t.prototype.emptyProp = new ut, $t.prototype.destroy = function() {},
  M([Jt, Rt, Lt, Vt, Nt], te),
  te.prototype.initElement =
      function(t, e, s) {
    this.initFrame(), this.initBaseData(t, e, s), this.initTransform(t, e, s),
        this.initRenderable(), this.initHierarchy(), this.initRendererElement(),
        this.createContainerElements(), this.createRenderableComponents(),
        !this.data.xt && e.progressiveLoad || this.buildAllItems(), this.hide()
  },
  te.prototype.prepareFrame =
      function(t) {
    if (this._mdf = !1, this.prepareRenderableFrame(t),
        this.prepareProperties(t, this.isInRange),
        this.isInRange || this.data.xt) {
      if (this.tm._placeholder)
        this.renderedFrame = t / this.data.sr;
      else {
        var e = this.tm.v;
        e === this.data.op && (e = this.data.op - 1), this.renderedFrame = e
      }
      var s, i = this.elements.length;
      for (this.completeLayers || this.checkLayers(this.renderedFrame),
           s = i - 1;
           0 <= s; s -= 1)
        (this.completeLayers || this.elements[s]) &&
            (this.elements[s].prepareFrame(
                 this.renderedFrame - this.layers[s].st),
             this.elements[s]._mdf && (this._mdf = !0))
    }
  },
  te.prototype.renderInnerContent =
      function() {
    var t, e = this.layers.length;
    for (t = 0; t < e; t += 1)
      (this.completeLayers || this.elements[t]) &&
          this.elements[t].renderFrame()
  },
  te.prototype.setElements =
      function(t) {
    this.elements = t
  },
  te.prototype.getElements =
      function() {
    return this.elements
  },
  te.prototype.destroyElements =
      function() {
    var t, e = this.layers.length;
    for (t = 0; t < e; t += 1) this.elements[t] && this.elements[t].destroy()
  },
  te.prototype.destroy =
      function() {
    this.destroyElements(), this.destroyBaseElement()
  },
  M([Jt, Rt, Zt, Lt, Vt, Nt], ee),
  ee.prototype.createContent =
      function() {
    var t = this.globalData.getAssetsPath(this.assetData);
    this.innerElem = x('image'),
    this.innerElem.setAttribute('width', this.assetData.w + 'px'),
    this.innerElem.setAttribute('height', this.assetData.h + 'px'),
    this.innerElem.setAttribute(
        'preserveAspectRatio',
        this.assetData.pr ||
            this.globalData.renderConfig.imagePreserveAspectRatio),
    this.innerElem.setAttributeNS('http://www.w3.org/1999/xlink', 'href', t),
    this.layerElement.appendChild(this.innerElem)
  },
  ee.prototype.sourceRectAtTime =
      function() {
    return this.sourceRect
  },
  M([ee], se),
  se.prototype.createContent =
      function() {
    var t = x('rect');
    t.setAttribute('width', this.data.sw),
        t.setAttribute('height', this.data.sh),
        t.setAttribute('fill', this.data.sc), this.layerElement.appendChild(t)
  },
  ie.prototype.prepareFrame =
      function(t) {
    if (this.prepareRenderableFrame(t, !0), this.prepareProperties(t, !0),
        this.tm._placeholder)
      this._currentTime = t / this.data.sr;
    else {
      var e = this.tm.v;
      this._currentTime = e
    }
  },
  M([zt, Jt, Vt], ie),
  ie.prototype.renderFrame =
      function() {
    this.isInRange && this._canPlay &&
        (this._isPlaying ?
             (!this.audio.playing() ||
              .1 < Math.abs(
                       this._currentTime / this.globalData.frameRate -
                       this.audio.seek())) &&
                 this.audio.seek(
                     this._currentTime / this.globalData.frameRate) :
             (this.audio.play(),
              this.audio.seek(this._currentTime / this.globalData.frameRate),
              this._isPlaying = !0))
  },
  ie.prototype.show = function() {},
  ie.prototype.hide =
      function() {
    this.audio.pause(), this._isPlaying = !1
  },
  ie.prototype.pause =
      function() {
    this.audio.pause(), this._isPlaying = !1, this._canPlay = !1
  },
  ie.prototype.resume =
      function() {
    this._canPlay = !0
  },
  ie.prototype.setRate =
      function(t) {
    this.audio.rate(t)
  },
  ie.prototype.volume =
      function(t) {
    this.audio.volume(t)
  },
  ie.prototype.getBaseElement =
      function() {
    return null
  },
  ie.prototype.destroy = function() {},
  ie.prototype.sourceRectAtTime = function() {},
  ie.prototype.initExpressions = function() {}, M([Mt, te, Zt], ae),
  M([Jt, Rt, Zt, Lt, Vt, Nt, $t], re),
  re.prototype.createContent =
      function() {
    this.data.singleShape && !this.globalData.fontManager.chars &&
        (this.textContainer = x('text'))
  },
  re.prototype.buildTextContents =
      function(t) {
    for (var e = 0, s = t.length, i = [], a = ''; e < s;)
      t[e] === String.fromCharCode(13) || t[e] === String.fromCharCode(3) ?
          (i.push(a), a = '') :
          a += t[e],
          e += 1;
    return i.push(a), i
  },
  re.prototype.buildNewText =
      function() {
    var t, e, s = this.textProperty.currentData;
    this.renderedLetters = D(s ? s.l.length : 0),
    s.fc ? this.layerElement.setAttribute('fill', this.buildColor(s.fc)) :
           this.layerElement.setAttribute('fill', 'rgba(0,0,0,0)'),
    s.sc &&
        (this.layerElement.setAttribute('stroke', this.buildColor(s.sc)),
         this.layerElement.setAttribute('stroke-width', s.sw)),
    this.layerElement.setAttribute('font-size', s.finalSize);
    var i = this.globalData.fontManager.getFontByName(s.f);
    if (i.fClass)
      this.layerElement.setAttribute('class', i.fClass);
    else {
      this.layerElement.setAttribute('font-family', i.fFamily);
      var a = s.fWeight, r = s.fStyle;
      this.layerElement.setAttribute('font-style', r),
          this.layerElement.setAttribute('font-weight', a)
    }
    this.layerElement.setAttribute('aria-label', s.t);
    var n, h = s.l || [], o = !!this.globalData.fontManager.chars;
    e = h.length;
    var l, p = this.mHelper, f = '', d = this.data.singleShape, m = 0, c = 0,
           u = !0, g = .001 * s.tr * s.finalSize;
    if (!d || o || s.sz) {
      var y, v, b = this.textSpans.length;
      for (t = 0; t < e; t += 1)
        o && d && 0 !== t ||
            (n = t < b ? this.textSpans[t] : x(o ? 'path' : 'text'),
             b <= t &&
                 (n.setAttribute('stroke-linecap', 'butt'),
                  n.setAttribute('stroke-linejoin', 'round'),
                  n.setAttribute('stroke-miterlimit', '4'),
                  this.textSpans[t] = n, this.layerElement.appendChild(n)),
             n.style.display = 'inherit'),
            p.reset(), p.scale(s.finalSize / 100, s.finalSize / 100),
            d &&
            (h[t].n && (m = -g, c += s.yOffset, c += u ? 1 : 0, u = !1),
             this.applyTextPropertiesToMatrix(s, p, h[t].line, m, c),
             m += h[t].l || 0, m += g),
            o ? (l = (y = (v = this.globalData.fontManager.getCharData(
                               s.finalText[t], i.fStyle,
                               this.globalData.fontManager.getFontByName(s.f)
                                   .fFamily)) &&
                              v.data ||
                          {})
                         .shapes ?
                     y.shapes[0].it :
                     [],
                 d ? f += this.createPathShape(p, l) :
                     n.setAttribute('d', this.createPathShape(p, l))) :
                (d &&
                     n.setAttribute(
                         'transform',
                         'translate(' + p.props[12] + ',' + p.props[13] + ')'),
                 n.textContent = h[t].val,
                 n.setAttributeNS(
                     'http://www.w3.org/XML/1998/namespace', 'xml:space',
                     'preserve'));
      d && n && n.setAttribute('d', f)
    } else {
      var _ = this.textContainer, k = 'start';
      switch (s.j) {
        case 1:
          k = 'end';
          break;
        case 2:
          k = 'middle';
          break;
        default:
          k = 'start'
      }
      _.setAttribute('text-anchor', k), _.setAttribute('letter-spacing', g);
      var A = this.buildTextContents(s.finalText);
      for (e = A.length, c = s.ps ? s.ps[1] + s.ascent : 0, t = 0; t < e;
           t += 1)
        (n = this.textSpans[t] || x('tspan')).textContent = A[t],
                                  n.setAttribute('x', 0),
                                  n.setAttribute('y', c),
                                  n.style.display = 'inherit', _.appendChild(n),
                                  this.textSpans[t] = n, c += s.finalLineHeight;
      this.layerElement.appendChild(_)
    }
    for (; t < this.textSpans.length;)
      this.textSpans[t].style.display = 'none', t += 1;
    this._sizeChanged = !0
  },
  re.prototype.sourceRectAtTime =
      function() {
    if (this.prepareFrame(this.comp.renderedFrame - this.data.st),
        this.renderInnerContent(), this._sizeChanged) {
      this._sizeChanged = !1;
      var t = this.layerElement.getBBox();
      this.bbox = {top: t.y, left: t.x, width: t.width, height: t.height}
    }
    return this.bbox
  },
  re.prototype.renderInnerContent =
      function() {
    if (!this.data.singleShape &&
        (this.textAnimator.getMeasures(
             this.textProperty.currentData, this.lettersChangedFlag),
         this.lettersChangedFlag || this.textAnimator.lettersChangedFlag)) {
      var t, e;
      this._sizeChanged = !0;
      var s, i, a = this.textAnimator.renderedLetters,
                r = this.textProperty.currentData.l;
      for (e = r.length, t = 0; t < e; t += 1)
        r[t].n ||
            (s = a[t], i = this.textSpans[t],
             s._mdf.m && i.setAttribute('transform', s.m),
             s._mdf.o && i.setAttribute('opacity', s.o),
             s._mdf.sw && i.setAttribute('stroke-width', s.sw),
             s._mdf.sc && i.setAttribute('stroke', s.sc),
             s._mdf.fc && i.setAttribute('fill', s.fc))
    }
  },
  M([Jt, Rt, Zt, Qt, Lt, Vt, Nt], ne),
  ne.prototype.initSecondaryElement = function() {},
  ne.prototype.identityMatrix = new I,
  ne.prototype.buildExpressionInterface = function() {},
  ne.prototype.createContent = function() {
    this.searchShapes(
        this.shapesData, this.itemsData, this.prevViewData, this.layerElement,
        0, [], !0),
        this.filterUniqueShapes()
  }, ne.prototype.filterUniqueShapes = function() {
    var t, e, s, i, a = this.shapes.length, r = this.stylesList.length, n = [],
                    h = !1;
    for (s = 0; s < r; s += 1) {
      for (i = this.stylesList[s], h = !1, t = n.length = 0; t < a; t += 1)
        -1 !== (e = this.shapes[t]).styles.indexOf(i) &&
            (n.push(e), h = e._isAnimated || h);
      1 < n.length && h && this.setShapesAsAnimated(n)
    }
  }, ne.prototype.setShapesAsAnimated = function(t) {
    var e, s = t.length;
    for (e = 0; e < s; e += 1) t[e].setAsAnimated()
  }, ne.prototype.createStyleElement = function(t, e) {
    var s, i = new qt(t, e), a = i.pElem;
    if ('st' === t.ty)
      s = new Wt(this, t, i);
    else if ('fl' === t.ty)
      s = new Xt(this, t, i);
    else if ('gf' === t.ty || 'gs' === t.ty) {
      s = new ('gf' === t.ty ? Ht : Yt)(this, t, i),
      this.globalData.defs.appendChild(s.gf),
      s.maskId &&
          (this.globalData.defs.appendChild(s.ms),
           this.globalData.defs.appendChild(s.of),
           a.setAttribute('mask', 'url(' + A + '#' + s.maskId + ')'))
    }
    return 'st' !== t.ty && 'gs' !== t.ty ||
               (a.setAttribute('stroke-linecap', this.lcEnum[t.lc] || 'round'),
                a.setAttribute('stroke-linejoin', this.ljEnum[t.lj] || 'round'),
                a.setAttribute('fill-opacity', '0'),
                1 === t.lj && a.setAttribute('stroke-miterlimit', t.ml)),
           2 === t.r && a.setAttribute('fill-rule', 'evenodd'),
           t.ln && a.setAttribute('id', t.ln),
           t.cl && a.setAttribute('class', t.cl),
           t.bm && (a.style['mix-blend-mode'] = E(t.bm)),
           this.stylesList.push(i), this.addToAnimatedContents(t, s), s
  }, ne.prototype.createGroupElement = function(t) {
    var e = new Gt;
    return t.ln && e.gr.setAttribute('id', t.ln),
           t.cl && e.gr.setAttribute('class', t.cl),
           t.bm && (e.gr.style['mix-blend-mode'] = E(t.bm)), e
  }, ne.prototype.createTransformElement = function(t, e) {
    var s = z.getTransformProperty(this, t, this), i = new jt(s, s.o, e);
    return this.addToAnimatedContents(t, i), i
  }, ne.prototype.createShapeElement = function(t, e, s) {
    var i = 4;
    'rc' === t.ty ? i = 5 : 'el' === t.ty ? i = 6 : 'sr' === t.ty && (i = 7);
    var a = new Bt(e, s, H.getShapeProp(this, t, i, this));
    return this.shapes.push(a), this.addShapeToModifiers(a),
           this.addToAnimatedContents(t, a), a
  }, ne.prototype.addToAnimatedContents = function(t, e) {
    for (var s = 0, i = this.animatedContents.length; s < i;) {
      if (this.animatedContents[s].element === e) return;
      s += 1
    }
    this.animatedContents.push(
        {fn: Kt.createRenderFunction(t), element: e, data: t})
  }, ne.prototype.setElementStyles = function(t) {
    var e, s = t.styles, i = this.stylesList.length;
    for (e = 0; e < i; e += 1)
      this.stylesList[e].closed || s.push(this.stylesList[e])
  }, ne.prototype.reloadShapes = function() {
    var t;
    this._isFirstFrame = !0;
    var e = this.itemsData.length;
    for (t = 0; t < e; t += 1) this.prevViewData[t] = this.itemsData[t];
    for (this.searchShapes(
             this.shapesData, this.itemsData, this.prevViewData,
             this.layerElement, 0, [], !0),
         this.filterUniqueShapes(), e = this.dynamicProperties.length, t = 0;
         t < e; t += 1)
      this.dynamicProperties[t].getValue();
    this.renderModifiers()
  }, ne.prototype.searchShapes = function(t, e, s, i, a, r, n) {
    var h, o, l, p, f, d, m = [].concat(r), c = t.length - 1, u = [], g = [];
    for (h = c; 0 <= h; h -= 1) {
      if ((d = this.searchProcessedElement(t[h])) ? e[h] = s[d - 1] :
                                                    t[h]._render = n,
          'fl' === t[h].ty || 'st' === t[h].ty || 'gf' === t[h].ty ||
              'gs' === t[h].ty)
        d ? e[h].style.closed = !1 : e[h] = this.createStyleElement(t[h], a),
            t[h]._render && i.appendChild(e[h].style.pElem), u.push(e[h].style);
      else if ('gr' === t[h].ty) {
        if (d)
          for (l = e[h].it.length, o = 0; o < l; o += 1)
            e[h].prevViewData[o] = e[h].it[o];
        else
          e[h] = this.createGroupElement(t[h]);
        this.searchShapes(
            t[h].it, e[h].it, e[h].prevViewData, e[h].gr, a + 1, m, n),
            t[h]._render && i.appendChild(e[h].gr)
      } else
        'tr' === t[h].ty ? (d || (e[h] = this.createTransformElement(t[h], i)),
                            p = e[h].transform, m.push(p)) :
            'sh' === t[h].ty || 'rc' === t[h].ty || 'el' === t[h].ty ||
                'sr' === t[h].ty ?
                           (d || (e[h] = this.createShapeElement(t[h], m, a)),
                            this.setElementStyles(e[h])) :
            'tm' === t[h].ty || 'rd' === t[h].ty || 'ms' === t[h].ty ||
                'pb' === t[h].ty ?
                           (d ? (f = e[h]).closed = !1 :
                                ((f = Y.getModifier(t[h].ty)).init(this, t[h]),
                                 e[h] = f, this.shapeModifiers.push(f)),
                            g.push(f)) :
                           'rp' === t[h].ty &&
                (d ? (f = e[h]).closed = !0 :
                     (f = Y.getModifier(t[h].ty),
                      (e[h] = f).init(this, t, h, e),
                      this.shapeModifiers.push(f), n = !1),
                 g.push(f));
      this.addProcessedElement(t[h], h + 1)
    }
    for (c = u.length, h = 0; h < c; h += 1) u[h].closed = !0;
    for (c = g.length, h = 0; h < c; h += 1) g[h].closed = !0
  }, ne.prototype.renderInnerContent = function() {
    var t;
    this.renderModifiers();
    var e = this.stylesList.length;
    for (t = 0; t < e; t += 1) this.stylesList[t].reset();
    for (this.renderShape(), t = 0; t < e; t += 1)
      (this.stylesList[t]._mdf || this._isFirstFrame) &&
          (this.stylesList[t].msElem &&
               (this.stylesList[t].msElem.setAttribute(
                    'd', this.stylesList[t].d),
                this.stylesList[t].d = 'M0 0' + this.stylesList[t].d),
           this.stylesList[t].pElem.setAttribute(
               'd', this.stylesList[t].d || 'M0 0'))
  }, ne.prototype.renderShape = function() {
    var t, e, s = this.animatedContents.length;
    for (t = 0; t < s; t += 1)
      e = this.animatedContents[t],
      (this._isFirstFrame || e.element._isAnimated) && !0 !== e.data &&
          e.fn(e.data, e.element, this._isFirstFrame)
  }, ne.prototype.destroy = function() {
    this.destroyBaseElement(), this.shapesData = null, this.itemsData = null
  };
  var he = [];
  function oe() {}
  var le = function() {
    var t = {}, a = [], i = 0, r = 0, n = 0, h = !0, o = !1;
    function s(t) {
      for (var e = 0, s = t.target; e < r;)
        a[e].animation === s &&
            (a.splice(e, 1), e -= 1, r -= 1, s.isPaused || f()),
            e += 1
    }
    function l(t, e) {
      if (!t) return null;
      for (var s = 0; s < r;) {
        if (a[s].elem === t && null !== a[s].elem) return a[s].animation;
        s += 1
      }
      var i = new pe;
      return d(i, t), i.setData(t, e), i
    }
    function p() {
      n += 1, c()
    }
    function f() {
      n -= 1
    }
    function d(t, e) {
      t.addEventListener('destroy', s), t.addEventListener('_active', p),
          t.addEventListener('_idle', f), a.push({elem: e, animation: t}),
          r += 1
    }
    function m(t) {
      var e, s = t - i;
      for (e = 0; e < r; e += 1) a[e].animation.advanceTime(s);
      i = t, n && !o ? window.requestAnimationFrame(m) : h = !0
    }
    function e(t) {
      i = t, window.requestAnimationFrame(m)
    }
    function c() {
      !o && n && h && (window.requestAnimationFrame(e), h = !1)
    }
    return t.registerAnimation = l, t.loadAnimation = function(t) {
      var e = new pe;
      return d(e, null), e.setParams(t), e
    }, t.setSpeed = function(t, e) {
      var s;
      for (s = 0; s < r; s += 1) a[s].animation.setSpeed(t, e)
    }, t.setDirection = function(t, e) {
      var s;
      for (s = 0; s < r; s += 1) a[s].animation.setDirection(t, e)
    }, t.play = function(t) {
      var e;
      for (e = 0; e < r; e += 1) a[e].animation.play(t)
    }, t.pause = function(t) {
      var e;
      for (e = 0; e < r; e += 1) a[e].animation.pause(t)
    }, t.stop = function(t) {
      var e;
      for (e = 0; e < r; e += 1) a[e].animation.stop(t)
    }, t.togglePause = function(t) {
      var e;
      for (e = 0; e < r; e += 1) a[e].animation.togglePause(t)
    }, t.searchAnimations = function(t, e, s) {
      var i,
          a = [].concat(
              [].slice.call(document.getElementsByClassName('lottie')),
              [].slice.call(document.getElementsByClassName('bodymovin'))),
          r = a.length;
      for (i = 0; i < r; i += 1)
        s && a[i].setAttribute('data-bm-type', s), l(a[i], t);
      if (e && 0 === r) {
        s || (s = 'svg');
        var n = document.getElementsByTagName('body')[0];
        n.innerText = '';
        var h = w('div');
        h.style.width = '100%', h.style.height = '100%',
        h.setAttribute('data-bm-type', s), n.appendChild(h), l(h, t)
      }
    }, t.resize = function() {
      var t;
      for (t = 0; t < r; t += 1) a[t].animation.resize()
    }, t.goToAndStop = function(t, e, s) {
      var i;
      for (i = 0; i < r; i += 1) a[i].animation.goToAndStop(t, e, s)
    }, t.destroy = function(t) {
      var e;
      for (e = r - 1; 0 <= e; e -= 1) a[e].animation.destroy(t)
    }, t.freeze = function() {
      o = !0
    }, t.unfreeze = function() {
      o = !1, c()
    }, t.setVolume = function(t, e) {
      var s;
      for (s = 0; s < r; s += 1) a[s].animation.setVolume(t, e)
    }, t.mute = function(t) {
      var e;
      for (e = 0; e < r; e += 1) a[e].animation.mute(t)
    }, t.unmute = function(t) {
      var e;
      for (e = 0; e < r; e += 1) a[e].animation.unmute(t)
    }, t.getRegisteredAnimations = function() {
      var t, e = a.length, s = [];
      for (t = 0; t < e; t += 1) s.push(a[t].animation);
      return s
    }, t
  }(), pe = function() {
    this._cbs = [], this.name = '', this.path = '', this.isLoaded = !1,
    this.currentFrame = 0, this.currentRawFrame = 0, this.firstFrame = 0,
    this.totalFrames = 0, this.frameRate = 0, this.frameMult = 0,
    this.playSpeed = 1, this.playDirection = 1, this.playCount = 0,
    this.animationData = {}, this.assets = [], this.isPaused = !0,
    this.autoplay = !1, this.loop = !0, this.renderer = null,
    this.animationID = S(), this.assetsPath = '', this.timeCompleted = 0,
    this.segmentPos = 0, this.isSubframeEnabled = i, this.segments = [],
    this._idle = !0, this._completedLoop = !1, this.projectInterface = {},
    this.imagePreloader = new rt, this.audioController = at(), this.markers = []
  };
  function fe() {
    this.effectElements = []
  }
  M([C], pe), pe.prototype.setParams = function(t) {
    (t.wrapper || t.container) && (this.wrapper = t.wrapper || t.container);
    var e = 'svg';
    switch (t.animType ? e = t.animType : t.renderer && (e = t.renderer), e) {
      case 'canvas':
        this.renderer = new CanvasRenderer(this, t.rendererSettings);
        break;
      case 'svg':
        this.renderer = new Mt(this, t.rendererSettings);
        break;
      default:
        this.renderer = new HybridRenderer(this, t.rendererSettings)
    }
    this.imagePreloader.setCacheType(e, this.renderer.globalData.defs),
        this.renderer.setProjectInterface(this.projectInterface),
        this.animType = e,
        '' === t.loop || null === t.loop || void 0 === t.loop || !0 === t.loop ?
        this.loop = !0 :
        !1 === t.loop ? this.loop = !1 :
                        this.loop = parseInt(t.loop, 10),
        this.autoplay = !('autoplay' in t) || t.autoplay,
        this.name = t.name ? t.name : '',
        this.autoloadSegments =
            !Object.prototype.hasOwnProperty.call(t, 'autoloadSegments') ||
        t.autoloadSegments,
        this.assetsPath = t.assetsPath, this.initialSegment = t.initialSegment,
        t.audioFactory && this.audioController.setAudioFactory(t.audioFactory),
        t.animationData ? this.configAnimation(t.animationData) :
                          t.path &&
            (-1 !== t.path.lastIndexOf('\\') ?
                 this.path = t.path.substr(0, t.path.lastIndexOf('\\') + 1) :
                 this.path = t.path.substr(0, t.path.lastIndexOf('/') + 1),
             this.fileName = t.path.substr(t.path.lastIndexOf('/') + 1),
             this.fileName =
                 this.fileName.substr(0, this.fileName.lastIndexOf('.json')),
             ot.load(t.path, this.configAnimation.bind(this), function() {
               this.trigger('data_failed')
             }.bind(this)))
  }, pe.prototype.setData = function(t, e) {
    e && 'object' != typeof e && (e = JSON.parse(e));
    var s = {wrapper: t, animationData: e}, i = t.attributes;
    s.path = i.getNamedItem('data-animation-path') ?
        i.getNamedItem('data-animation-path').value :
        i.getNamedItem('data-bm-path') ? i.getNamedItem('data-bm-path').value :
        i.getNamedItem('bm-path')      ? i.getNamedItem('bm-path').value :
                                         '',
    s.animType = i.getNamedItem('data-anim-type') ?
        i.getNamedItem('data-anim-type').value :
        i.getNamedItem('data-bm-type') ? i.getNamedItem('data-bm-type').value :
        i.getNamedItem('bm-type')      ? i.getNamedItem('bm-type').value :
        i.getNamedItem('data-bm-renderer') ?
                                    i.getNamedItem('data-bm-renderer').value :
        i.getNamedItem('bm-renderer') ? i.getNamedItem('bm-renderer').value :
                                        'canvas';
    var a = i.getNamedItem('data-anim-loop') ?
        i.getNamedItem('data-anim-loop').value :
        i.getNamedItem('data-bm-loop') ? i.getNamedItem('data-bm-loop').value :
        i.getNamedItem('bm-loop')      ? i.getNamedItem('bm-loop').value :
                                         '';
    'false' === a    ? s.loop = !1 :
        'true' === a ? s.loop = !0 :
                       '' !== a && (s.loop = parseInt(a, 10));
    var r = i.getNamedItem('data-anim-autoplay') ?
        i.getNamedItem('data-anim-autoplay').value :
        i.getNamedItem('data-bm-autoplay') ?
        i.getNamedItem('data-bm-autoplay').value :
        !i.getNamedItem('bm-autoplay') || i.getNamedItem('bm-autoplay').value;
    s.autoplay = 'false' !== r,
    s.name = i.getNamedItem('data-name') ? i.getNamedItem('data-name').value :
        i.getNamedItem('data-bm-name') ? i.getNamedItem('data-bm-name').value :
        i.getNamedItem('bm-name')      ? i.getNamedItem('bm-name').value :
                                         '',
    'false' ===
            (i.getNamedItem('data-anim-prerender') ?
                 i.getNamedItem('data-anim-prerender').value :
                 i.getNamedItem('data-bm-prerender') ?
                 i.getNamedItem('data-bm-prerender').value :
                 i.getNamedItem('bm-prerender') ?
                 i.getNamedItem('bm-prerender').value :
                 '') &&
        (s.prerender = !1),
    this.setParams(s)
  }, pe.prototype.includeLayers = function(t) {
    t.op > this.animationData.op &&
        (this.animationData.op = t.op,
         this.totalFrames = Math.floor(t.op - this.animationData.ip));
    var e, s, i = this.animationData.layers, a = i.length, r = t.layers,
              n = r.length;
    for (s = 0; s < n; s += 1)
      for (e = 0; e < a;) {
        if (i[e].id === r[s].id) {
          i[e] = r[s];
          break
        }
        e += 1
      }
    if ((t.chars || t.fonts) &&
            (this.renderer.globalData.fontManager.addChars(t.chars),
             this.renderer.globalData.fontManager.addFonts(
                 t.fonts, this.renderer.globalData.defs)),
        t.assets)
      for (a = t.assets.length, e = 0; e < a; e += 1)
        this.animationData.assets.push(t.assets[e]);
    this.animationData.__complete = !1,
    L.completeData(this.animationData, this.renderer.globalData.fontManager),
    this.renderer.includeLayers(t.layers), h && h.initExpressions(this),
    this.loadNextSegment()
  }, pe.prototype.loadNextSegment = function() {
    var t = this.animationData.segments;
    if (!t || 0 === t.length || !this.autoloadSegments)
      return this.trigger('data_ready'),
             void (this.timeCompleted = this.totalFrames);
    var e = t.shift();
    this.timeCompleted = e.time * this.frameRate;
    var s = this.path + this.fileName + '_' + this.segmentPos + '.json';
    this.segmentPos += 1, ot.load(s, this.includeLayers.bind(this), function() {
      this.trigger('data_failed')
    }.bind(this))
  }, pe.prototype.loadSegments = function() {
    this.animationData.segments || (this.timeCompleted = this.totalFrames),
        this.loadNextSegment()
  }, pe.prototype.imagesLoaded = function() {
    this.trigger('loaded_images'), this.checkLoaded()
  }, pe.prototype.preloadImages = function() {
    this.imagePreloader.setAssetsPath(this.assetsPath),
        this.imagePreloader.setPath(this.path),
        this.imagePreloader.loadAssets(
            this.animationData.assets, this.imagesLoaded.bind(this))
  }, pe.prototype.configAnimation = function(t) {
    if (this.renderer) try {
        this.animationData = t,
        this.initialSegment ?
            (this.totalFrames =
                 Math.floor(this.initialSegment[1] - this.initialSegment[0]),
             this.firstFrame = Math.round(this.initialSegment[0])) :
            (this.totalFrames =
                 Math.floor(this.animationData.op - this.animationData.ip),
             this.firstFrame = Math.round(this.animationData.ip)),
        this.renderer.configAnimation(t), t.assets || (t.assets = []),
        this.assets = this.animationData.assets,
        this.frameRate = this.animationData.fr,
        this.frameMult = this.animationData.fr / 1e3,
        this.renderer.searchExtraCompositions(t.assets),
        this.markers = Tt(t.markers || []), this.trigger('config_ready'),
        this.preloadImages(), this.loadSegments(), this.updaFrameModifier(),
        this.waitForFontsLoaded(), this.isPaused && this.audioController.pause()
      } catch (t) {
        this.triggerConfigError(t)
      }
  }, pe.prototype.waitForFontsLoaded = function() {
    this.renderer &&
        (this.renderer.globalData.fontManager.isLoaded ?
             this.checkLoaded() :
             setTimeout(this.waitForFontsLoaded.bind(this), 20))
  }, pe.prototype.checkLoaded = function() {
    !this.isLoaded && this.renderer.globalData.fontManager.isLoaded &&
        (this.imagePreloader.loadedImages() ||
         'canvas' !== this.renderer.rendererType) &&
        this.imagePreloader.loadedFootages() &&
        (this.isLoaded = !0,
         L.completeData(
             this.animationData, this.renderer.globalData.fontManager),
         h && h.initExpressions(this), this.renderer.initItems(),
         setTimeout(function() {
           this.trigger('DOMLoaded')
         }.bind(this), 0), this.gotoFrame(), this.autoplay && this.play())
  }, pe.prototype.resize = function() {
    this.renderer.updateContainerSize()
  }, pe.prototype.setSubframe = function(t) {
    this.isSubframeEnabled = !!t
  }, pe.prototype.gotoFrame = function() {
    this.currentFrame =
        this.isSubframeEnabled ? this.currentRawFrame : ~~this.currentRawFrame,
    this.timeCompleted !== this.totalFrames &&
        this.currentFrame > this.timeCompleted &&
        (this.currentFrame = this.timeCompleted),
    this.trigger('enterFrame'), this.renderFrame()
  }, pe.prototype.renderFrame = function() {
    if (!1 !== this.isLoaded && this.renderer) try {
        this.renderer.renderFrame(this.currentFrame + this.firstFrame)
      } catch (t) {
        this.triggerRenderFrameError(t)
      }
  }, pe.prototype.play = function(t) {
    t && this.name !== t ||
        !0 === this.isPaused &&
            (this.isPaused = !1, this.audioController.resume(),
             this._idle && (this._idle = !1, this.trigger('_active')))
  }, pe.prototype.pause = function(t) {
    t && this.name !== t ||
        !1 === this.isPaused &&
            (this.isPaused = !0, this._idle = !0, this.trigger('_idle'),
             this.audioController.pause())
  }, pe.prototype.togglePause = function(t) {
    t && this.name !== t || (!0 === this.isPaused ? this.play() : this.pause())
  }, pe.prototype.stop = function(t) {
    t && this.name !== t ||
        (this.pause(), this.playCount = 0, this._completedLoop = !1,
         this.setCurrentRawFrameValue(0))
  }, pe.prototype.getMarkerData = function(t) {
    for (var e, s = 0; s < this.markers.length; s += 1)
      if ((e = this.markers[s]).payload && e.payload.name === t) return e;
    return null
  }, pe.prototype.goToAndStop = function(t, e, s) {
    if (!s || this.name === s) {
      var i = Number(t);
      if (isNaN(i)) {
        var a = this.getMarkerData(t);
        a && this.goToAndStop(a.time, !0)
      } else
        e ? this.setCurrentRawFrameValue(t) :
            this.setCurrentRawFrameValue(t * this.frameModifier);
      this.pause()
    }
  }, pe.prototype.goToAndPlay = function(t, e, s) {
    if (!s || this.name === s) {
      var i = Number(t);
      if (isNaN(i)) {
        var a = this.getMarkerData(t);
        a &&
            (a.duration ? this.playSegments([a.time, a.time + a.duration], !0) :
                          this.goToAndStop(a.time, !0))
      } else
        this.goToAndStop(i, e, s);
      this.play()
    }
  }, pe.prototype.advanceTime = function(t) {
    if (!0 !== this.isPaused && !1 !== this.isLoaded) {
      var e = this.currentRawFrame + t * this.frameModifier, s = !1;
      e >= this.totalFrames - 1 && 0 < this.frameModifier ?
          this.loop && this.playCount !== this.loop ?
          e >= this.totalFrames ?
          (this.playCount += 1,
           this.checkSegments(e % this.totalFrames) ||
               (this.setCurrentRawFrameValue(e % this.totalFrames),
                this._completedLoop = !0, this.trigger('loopComplete'))) :
          this.setCurrentRawFrameValue(e) :
          this.checkSegments(e > this.totalFrames ? e % this.totalFrames : 0) ||
                  (s = !0, e = this.totalFrames - 1) :
          e < 0 ? this.checkSegments(e % this.totalFrames) ||
              (!this.loop || this.playCount-- <= 0 && !0 !== this.loop ?
                   (s = !0, e = 0) :
                   (this.setCurrentRawFrameValue(
                        this.totalFrames + e % this.totalFrames),
                    this._completedLoop ? this.trigger('loopComplete') :
                                          this._completedLoop = !0)) :
                  this.setCurrentRawFrameValue(e),
          s &&
          (this.setCurrentRawFrameValue(e), this.pause(),
           this.trigger('complete'))
    }
  }, pe.prototype.adjustSegment = function(t, e) {
    this.playCount = 0,
    t[1] < t[0] ?
        (0 < this.frameModifier &&
             (this.playSpeed < 0 ? this.setSpeed(-this.playSpeed) :
                                   this.setDirection(-1)),
         this.totalFrames = t[0] - t[1], this.timeCompleted = this.totalFrames,
         this.firstFrame = t[1],
         this.setCurrentRawFrameValue(this.totalFrames - .001 - e)) :
        t[1] > t[0] &&
            (this.frameModifier < 0 &&
                 (this.playSpeed < 0 ? this.setSpeed(-this.playSpeed) :
                                       this.setDirection(1)),
             this.totalFrames = t[1] - t[0],
             this.timeCompleted = this.totalFrames, this.firstFrame = t[0],
             this.setCurrentRawFrameValue(.001 + e)),
    this.trigger('segmentStart')
  }, pe.prototype.setSegment = function(t, e) {
    var s = -1;
    this.isPaused &&
        (this.currentRawFrame + this.firstFrame < t ?
             s = t :
             this.currentRawFrame + this.firstFrame > e && (s = e - t)),
        this.firstFrame = t, this.totalFrames = e - t,
        this.timeCompleted = this.totalFrames,
        -1 !== s && this.goToAndStop(s, !0)
  }, pe.prototype.playSegments = function(t, e) {
    if (e && (this.segments.length = 0), 'object' == typeof t[0]) {
      var s, i = t.length;
      for (s = 0; s < i; s += 1) this.segments.push(t[s])
    } else
      this.segments.push(t);
    this.segments.length && e && this.adjustSegment(this.segments.shift(), 0),
        this.isPaused && this.play()
  }, pe.prototype.resetSegments = function(t) {
    this.segments.length = 0,
    this.segments.push([this.animationData.ip, this.animationData.op]),
    t && this.checkSegments(0)
  }, pe.prototype.checkSegments = function(t) {
    return !!this.segments.length &&
        (this.adjustSegment(this.segments.shift(), t), !0)
  }, pe.prototype.destroy = function(t) {
    t && this.name !== t || !this.renderer ||
        (this.renderer.destroy(), this.imagePreloader.destroy(),
         this.trigger('destroy'), this._cbs = null, this.onEnterFrame = null,
         this.onLoopComplete = null, this.onComplete = null,
         this.onSegmentStart = null, this.onDestroy = null,
         this.renderer = null, this.renderer = null, this.imagePreloader = null,
         this.projectInterface = null)
  }, pe.prototype.setCurrentRawFrameValue = function(t) {
    this.currentRawFrame = t, this.gotoFrame()
  }, pe.prototype.setSpeed = function(t) {
    this.playSpeed = t, this.updaFrameModifier()
  }, pe.prototype.setDirection = function(t) {
    this.playDirection = t < 0 ? -1 : 1, this.updaFrameModifier()
  }, pe.prototype.setVolume = function(t, e) {
    e && this.name !== e || this.audioController.setVolume(t)
  }, pe.prototype.getVolume = function() {
    return this.audioController.getVolume()
  }, pe.prototype.mute = function(t) {
    t && this.name !== t || this.audioController.mute()
  }, pe.prototype.unmute = function(t) {
    t && this.name !== t || this.audioController.unmute()
  }, pe.prototype.updaFrameModifier = function() {
    this.frameModifier = this.frameMult * this.playSpeed * this.playDirection,
    this.audioController.setRate(this.playSpeed * this.playDirection)
  }, pe.prototype.getPath = function() {
    return this.path
  }, pe.prototype.getAssetsPath = function(t) {
    var e = '';
    if (t.e)
      e = t.p;
    else if (this.assetsPath) {
      var s = t.p;
      -1 !== s.indexOf('images/') && (s = s.split('/')[1]),
          e = this.assetsPath + s
    } else
      e = this.path, e += t.u ? t.u : '', e += t.p;
    return e
  }, pe.prototype.getAssetData = function(t) {
    for (var e = 0, s = this.assets.length; e < s;) {
      if (t === this.assets[e].id) return this.assets[e];
      e += 1
    }
    return null
  }, pe.prototype.hide = function() {
    this.renderer.hide()
  }, pe.prototype.show = function() {
    this.renderer.show()
  }, pe.prototype.getDuration = function(t) {
    return t ? this.totalFrames : this.totalFrames / this.frameRate
  }, pe.prototype.trigger = function(t) {
    if (this._cbs && this._cbs[t]) switch (t) {
        case 'enterFrame':
          this.triggerEvent(
              t,
              new o(
                  t, this.currentFrame, this.totalFrames, this.frameModifier));
          break;
        case 'loopComplete':
          this.triggerEvent(
              t, new p(t, this.loop, this.playCount, this.frameMult));
          break;
        case 'complete':
          this.triggerEvent(t, new l(t, this.frameMult));
          break;
        case 'segmentStart':
          this.triggerEvent(t, new m(t, this.firstFrame, this.totalFrames));
          break;
        case 'destroy':
          this.triggerEvent(t, new c(t, this));
          break;
        default:
          this.triggerEvent(t)
      }
    'enterFrame' === t && this.onEnterFrame &&
        this.onEnterFrame.call(
            this,
            new o(t, this.currentFrame, this.totalFrames, this.frameMult)),
        'loopComplete' === t && this.onLoopComplete &&
        this.onLoopComplete.call(
            this, new p(t, this.loop, this.playCount, this.frameMult)),
        'complete' === t && this.onComplete &&
        this.onComplete.call(this, new l(t, this.frameMult)),
        'segmentStart' === t && this.onSegmentStart &&
        this.onSegmentStart.call(
            this, new m(t, this.firstFrame, this.totalFrames)),
        'destroy' === t && this.onDestroy &&
        this.onDestroy.call(this, new c(t, this))
  }, pe.prototype.triggerRenderFrameError = function(t) {
    var e = new u(t, this.currentFrame);
    this.triggerEvent('error', e), this.onError && this.onError.call(this, e)
  }, pe.prototype.triggerConfigError = function(t) {
    var e = new g(t, this.currentFrame);
    this.triggerEvent('error', e), this.onError && this.onError.call(this, e)
  };
  var lottie = {};
  function de() {
    !0 === ce ? le.searchAnimations(ue, ce, ge) : le.searchAnimations()
  }
  lottie.play = le.play, lottie.pause = le.pause,
  lottie.setLocationHref =
      function(t) {
    A = t
  },
  lottie.togglePause = le.togglePause, lottie.setSpeed = le.setSpeed,
  lottie.setDirection = le.setDirection, lottie.stop = le.stop,
  lottie.searchAnimations = de, lottie.registerAnimation = le.registerAnimation,
  lottie.loadAnimation =
      function(t) {
    return !0 === ce && (t.animationData = JSON.parse(ue)), le.loadAnimation(t)
  },
  lottie.setSubframeRendering =
      function(t) {
    i = t
  },
  lottie.resize = le.resize, lottie.goToAndStop = le.goToAndStop,
  lottie.destroy = le.destroy,
  lottie.setQuality =
      function(t) {
    if ('string' == typeof t) switch (t) {
        case 'high':
          P = 200;
          break;
        default:
        case 'medium':
          P = 50;
          break;
        case 'low':
          P = 10
      }
    else
      !isNaN(t) && 1 < t && (P = t);
    r(!(50 <= P))
  },
  lottie.inBrowser =
      function() {
    return 'undefined' != typeof navigator
  },
  lottie.installPlugin =
      function(t, e) {
    'expressions' === t && (h = e)
  },
  lottie.freeze = le.freeze, lottie.unfreeze = le.unfreeze,
  lottie.setVolume = le.setVolume, lottie.mute = le.mute,
  lottie.unmute = le.unmute,
  lottie.getRegisteredAnimations = le.getRegisteredAnimations,
  lottie.__getFactory = function(t) {
    switch (t) {
      case 'propertyFactory':
        return R;
      case 'shapePropertyFactory':
        return H;
      case 'matrix':
        return I;
      default:
        return null
    }
  }, lottie.version = '5.7.8';
  var me, ce = '__[STANDALONE]__', ue = '__[ANIMATIONDATA]__', ge = '';
  if (ce) {
    var ye = document.getElementsByTagName('script'),
        ve = ye[ye.length - 1] || {src: ''};
    me = ve.src.replace(/^[^\?]+\??/, ''), ge = function(t) {
      for (var e = me.split('&'), s = 0; s < e.length; s += 1) {
        var i = e[s].split('=');
        if (decodeURIComponent(i[0]) == t) return decodeURIComponent(i[1])
      }
      return null
    }('renderer')
  }
  var be = setInterval(function() {
    'complete' === document.readyState && (clearInterval(be), de())
  }, 100);
  return lottie;
}));