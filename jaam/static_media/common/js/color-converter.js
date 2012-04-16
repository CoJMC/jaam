/* adapted from the HSL color picker at http://hslpicker.com/
 * source at http://github.com/imathis/hsl-color-picker
 */

String.prototype.clean = clean;
function clean() {
    return this.replace(/\s+/g, " ").trim();
}

Number.prototype.round = round;
function round(a) {
    a = Math.pow(10, a || 0).toFixed(a < 0 ? -a : 0);
    return Math.round(this * a) / a;
}

function Color(color, type) {
    if (type == 'hex' && this.validHex(color)) {
        this.setHex(color);
    } else if (type == 'hsl' && this.validHsl(color)) {
        this.setHsl(color);
    } else if (type == 'rgb' && this.validRgb(color)) {
        this.setRgb(color);
    } else if (typeof(color) == 'string') {
        if (this.validHex(color)) {
            this.setHex(color);
        } else if (this.validRgb(color)) {
            this.setRgb(color);
        } else if (this.validHsl(color)) {
            this.setHsl(color);
        }
    }
}
Color.prototype.setHsl = setHsl;
Color.prototype.setRgb = setRgb;
Color.prototype.setHex = setHex;
Color.prototype.adjustLum = adjustLum;
Color.prototype.adjustSat = adjustSat;
Color.prototype.adjustSatLum = adjustSatLum;
Color.prototype.hex = hex;
Color.prototype.rgb = rgb;
Color.prototype.hsl = hsl;
Color.prototype.rgbStr = rgbStr;
Color.prototype.hslStr = hslStr;
Color.prototype.hue = hue;
Color.prototype.sat = sat;
Color.prototype.lum = lum;
Color.prototype.red = red;
Color.prototype.green = green;
Color.prototype.blue = blue;
Color.prototype.validHex = validHex;
Color.prototype.validRgb = validRgb;
Color.prototype.validHsl = validHsl;
Color.prototype.toRgb = toRgb;
Color.prototype.toHsl = toHsl;
Color.prototype.toHex = toHex;
Color.prototype.hslToHex = hslToHex;
Color.prototype.hexToHsl = hexToHsl;
Color.prototype.rgbToHex = rgbToHex;
Color.prototype.toLongHex = toLongHex;
Color.prototype.hexToRgb = hexToRgb;
Color.prototype.hslToRgb = hslToRgb;
Color.prototype.hueToRgb = hueToRgb;
Color.prototype.rgbToHsl = rgbToHsl;

function setHsl(color) {
    this._hsl = this.toHsl(color);
    this._rgb = this.hslToRgb(this._hsl);
    this._hex = this.rgbToHex(this._rgb);
}

function setRgb(color) {
    this._rgb = this.toRgb(color);
    this._hsl = this.rgbToHsl(this._rgb);
    this._hex = this.rgbToHex(this._rgb);
}

function setHex(color) {
    this._hex = this.toHex(color);
    this._rgb = this.hexToRgb(this._hex);
    this._hsl = this.rgbToHsl(this._rgb);
}

function adjustLum(l, color){
    color = (typeof(color) == 'undefined') ? this._hsl : color;
    return this.hslStr([color[0], color[1], color[2] + l]);
}

function adjustSat(s, color){
    color = (typeof(color) == 'undefined') ? this._hsl : color;
    return this.hslStr([color[0], color[1] + s, color[2]]);
}

function adjustSatLum(s, l, color){
    color = (typeof(color) == 'undefined') ? this._hsl : color;
    return this.hslStr([color[0], color[1] + s, color[2] + l]);
}

function hex(notStr) {
    return (notStr) ? this._hex : '#'+this._hex;
}

function rgb(notStr) {
    return (notStr) ? this._rgb : this.rgbStr(this._rgb);
}

function hsl(notStr) {
    return (notStr) ? this._hsl : this.hslStr(this._hsl);
}

function rgbStr(rgb) {
return "rgb(" + rgb.join(", ") + ")";
}

function hslStr(hsl) {
    return "hsl("+ hsl[0] +", "+ hsl[1] +"%, "+ hsl[2] +"%)";
}

function hue(){
    return this.hsl(true)[0];
}

function sat(){
    return this.hsl(true)[1];
}

function lum() {
    return this.hsl(true)[2];
}

function red() {
    return this.rgb(true)[0];
}

function green() {
    return this.rgb(true)[1];
}

function blue() {
    return this.rgb(true)[2];
}

function validHex(color){
    var regex = /^(#)?([0-9a-fA-F]{3})([0-9a-fA-F]{3})?$/;
    return regex.test(color);
}

function validRgb(color) {
    color = (typeof(color) == 'array') ? color : this.toRgb(color);
    return color.every(function(item, index){ return (item >= 0) && (item <= 255) })
}

function validHsl(color) {
    color = (typeof(color) == 'array') ? color : this.toHsl(color);
    return color.every(function(item, index){ return (index == 0 && item >= 0 && item <= 360) || (index > 0 && item >= 0 && item <= 100) });
}

function toRgb(rgb){
    if (typeof(rgb) == 'string')
        return rgb.replace(/rgb\(/, '').replace(/\)/, '').replace(/;/, '').clean().split(',').map(function(item, index) { return parseFloat(item); });
    else
        return rgb;
}

function toHsl(hsl){
if (typeof(hsl) == 'string')
    return hsl.replace(/hsl\(/, '').replace(/\)/, '').replace(/;/, '').replace(/\%/, '').clean().split(',').map(function(item, index) { return parseFloat(item); });
else
    return hsl;
}

function toHex(hex){
    return hex.replace(/\#/, '').clean();
}

function hslToHex(hsl) {
    return this.rgbToHex(this.hslToRgb(hsl));
}

function hexToHsl(hex){
    return this.rgbToHsl(this.hexToRgb(hex));
}

function rgbToHex(rgb) {
    var r = parseFloat(rgb[0]).toString(16);
    var g = parseFloat(rgb[1]).toString(16);
    var b = parseFloat(rgb[2]).toString(16);
    if (r.length === 1) r = "0" + r;
    if (g.length === 1) g = "0" + g;
    if (b.length === 1) b = "0" + b;
    return (r + g + b).toUpperCase();
}

function toLongHex(hex){
    if(hex.length < 6){
        return hex[0]+hex[0]+hex[1]+hex[1]+hex[2]+hex[2];
    } else {
        return hex;
    }
}

function hexToRgb(hex) {
    hex = this.toLongHex(hex);
    var r = parseInt(hex.substring(0,2), 16);
    var g = parseInt(hex.substring(2,4), 16);
    var b = parseInt(hex.substring(4,6), 16);
    
    return [r, g, b];
}

function hslToRgb(hsl) {
    var h = parseInt(hsl[0]) / 360;
    var s = parseInt(hsl[1]) / 100;
    var l = parseInt(hsl[2]) / 100;
    
    if (l <= 0.5) var q = l * (1 + s);
    else var q = l + s - (l * s);
    
    var p = 2 * l - q;
    var tr = h + (1 / 3);
    var tg = h;
    var tb = h - (1 / 3);
    
    var r = Math.round(this.hueToRgb(p, q, tr) * 255);
    var g = Math.round(this.hueToRgb(p, q, tg) * 255);
    var b = Math.round(this.hueToRgb(p, q, tb) * 255);
    return [r, g, b];
}

function hueToRgb(p, q, h) {
    if (h < 0) h += 1;
    else if (h > 1) h -= 1;
    
    if ((h * 6) < 1) return p + (q - p) * h * 6;
    else if ((h * 2) < 1) return q;
    else if ((h * 3) < 2) return p + (q - p) * ((2 / 3) - h) * 6;
    else return p;
}

function rgbToHsl(rgb) {
    var r = parseFloat(rgb[0]) / 255;
    var g = parseFloat(rgb[1]) / 255;
    var b = parseFloat(rgb[2]) / 255;
    var max = Math.max(r, g, b);
    var min = Math.min(r, g, b);
    var diff = max - min;
    var add = max + min;
    
    if (min === max) var h = 0;
    else if (r === max) var h = ((60 * (g - b) / diff) + 360) % 360;
    else if (g === max) var h = (60 * (b - r) / diff) + 120;
    else var h = (60 * (r - g) / diff) + 240;
    
    var l = 0.5 * add;
    
    if (l === 0) var s = 0;
    else if (l === 1) var s = 1;
    else if (l <= 0.5) var s = diff / add;
    else var s = diff / (2 - add);
    
    h = h.round();
    s = (s*100).round();
    l = (l*100).round();
    
    return [h, s, l];
}