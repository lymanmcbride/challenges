import re


def listOFWords(string):
    filteredString = re.sub(r'[^\w\s]', "", string)
    filteredArray = filteredString.split(" ")
    items = {}
    for item in filteredArray:
        if item in items.keys():
            items[item] += 1
        else:
            items[item] = 1
    for item in items.keys():
        printedString = "{}: {}".format(item, items[item])
        print(printedString)



sentence = """<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta charset="UTF-8"><meta content="origin" name="referrer"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><link href="/manifest?pwa=webhp" crossorigin="use-credentials" rel="manifest"><title>Google</title><script nonce="k5Jw/eNXCbD5/lgt7TFi5g==">(function(){window.google={kEI:'AwN6YNcGtLjQ8Q-03p-ABg',kEXPI:'31',u:'abb3f581',kBL:'f_Ps'};google.sn='webhp';google.kHL='en';})();(function(){
var f,h=[];function k(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||f}function l(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b}
function m(a,b,c,d,g){var e="";c||-1!=b.search("&ei=")||(e="&ei="+k(d),-1==b.search("&lei=")&&(d=l(d))&&(e+="&lei="+d));d="";!c&&window._cshid&&-1==b.search("&cshid=")&&"slh"!=a&&(d="&cshid="+window._cshid);c=c||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+e+"&zx="+Date.now()+d;/^http:/i.test(c)&&"https:"==window.location.protocol&&(google.ml&&google.ml(Error("a"),!1,{src:c,glmm:1}),c="");return c};f=google.kEI;google.getEI=k;google.getLEI=l;google.ml=function(){return null};google.log=function(a,b,c,d,g){if(c=m(a,b,c,d,g)){a=new Image;var e=h.length;h[e]=a;a.onerror=a.onload=a.onabort=function(){delete h[e]};a.src=c}};google.logUrl=m;}).call(this);(function(){google.y={};google.sy=[];google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.sx=function(a){google.sy.push(a)};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};google.bx=!1;google.lx=function(){};}).call(this);google.f={};(function(){
document.documentElement.addEventListener("submit",function(b){var a;if(a=b.target){var c=a.getAttribute("data-submitfalse");a="1"==c||"q"==c&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener("click",function(b){var a;a:{for(a=b.target;a&&a!=document.documentElement;a=a.parentElement)if("A"==a.tagName){a="1"==a.getAttribute("data-nohref");break a}a=!1}a&&b.preventDefault()},!0);}).call(this);(function(){google.hs={h:true,peh:true,sie:false};})();(function(){google.c={biml:true,btfi:false,datfo:false,gl:true,lhc:false,ll:false,lmv:false};(function(){
var e=window.performance;google.timers={};google.startTick=function(a){google.timers[a]={t:{start:Date.now()},e:{},m:{}}};google.tick=function(a,b,c){google.timers[a]||google.startTick(a);c=void 0!==c?c:Date.now();b instanceof Array||(b=[b]);for(var d=0,f;f=b[d++];)google.timers[a].t[f]=c};google.c.e=function(a,b,c){google.timers[a].e[b]=c};google.c.b=function(a){var b=google.timers.load.m;b[a]&&google.ml(Error("a"),!1,{m:a});b[a]=!0};google.c.u=function(a){var b=google.timers.load.m;if(b[a]){b[a]=!1;for(a in b)if(b[a])return;google.csiReport()}else google.ml(Error("b"),!1,{m:a})};function g(a,b,c,d){a.addEventListener?a.addEventListener(b,c,d||!1):a.attachEvent&&a.attachEvent("on"+b,c)}function h(a,b,c,d){a.addEventListener?a.removeEventListener(b,c,d||!1):a.attachEvent&&a.detachEvent("on"+b,c)}google.rll=function(a,b,c){var d=function(f){c(f);h(a,"load",d);h(a,"error",d)};g(a,"load",d);b&&g(a,"error",d)};google.aft=function(a){a.setAttribute("data-iml",Date.now())};google.startTick("load");var k=google.timers.load;a:{var l=k.t;if(e){var m=e.timing;if(m){var n=m.navigationStart,p=m.responseStart;if(p>n&&p<=l.start){l.start=p;k.wsrt=p-n;break a}}e.now&&(k.wsrt=Math.floor(e.now()))}}google.c.b("pr");google.c.b("xe");if(google.c.gl){var q=function(a){a&&google.aft(a.target)};g(document.documentElement,"load",q,!0);google.c.glu=function(){h(document.documentElement,"load",q,!0)}};}).call(this);})();(function(){
function k(){return window.performance&&window.performance.navigation&&window.performance.navigation.type};function m(a,c){return!a||!c&&q(a)?0:a.getBoundingClientRect?r(a,c,function(b){return b.getBoundingClientRect()}):1}function q(a){return"none"==a.style.display?!0:document.defaultView&&document.defaultView.getComputedStyle?(a=document.defaultView.getComputedStyle(a),!!a&&("hidden"==a.visibility||"0px"==a.height&&"0px"==a.width)):!1}
function r(a,c,b){var d=b(a);a=d.left+window.pageXOffset;b=d.top+window.pageYOffset;var f=d.width;d=d.height;var e=0;if(!c&&0>=d&&0>=f)return e;c=window.innerHeight||document.documentElement.clientHeight;0>b+d?e=2:b>=c&&(e=4);if(0>a+f||a>=(window.innerWidth||document.documentElement.clientWidth))e|=8;e||(e=1,b+d>c&&(e|=4));return e};var t=window.location,u="aft frt hct prt pprt sct".split(" ");function v(a){return(a=t.search.match(new RegExp("[?&]"+a+"=(\\d+)")))?Number(a[1]):-1};var w=window.innerHeight||document.documentElement.clientHeight,x=0,y=0,z=0,A=0,B=0,C=0,D=0,E=!0,F=!0,I=-1;function J(a,c,b,d){var f=google.timers.load.t[a];f&&(b||d&&null!=c&&c<f)||google.tick("load",a,c)}function K(a,c,b){a&&(J("frt",b,!1,!0),++A,L());c&&(J("aft",b,!1,!0),++C,L());J("iml",b,!1,!0);++y;(google.c.biml||c)&&M()}function M(){var a=google.c.biml?y==x:B==C;!F&&a&&google.c.u("il")}
function L(){if(!E){var a=C==B,c=A==z;if(a&&c){google.c.e("load","ima",String(B));google.c.e("load","imad",String(D));google.c.e("load","aftp",String(Math.round(I)));var b=google.timers.load,d=b.m;if(!d||!d.prs){var f=k()?0:v("qsubts");0<f&&(d=v("fbts"),0<d&&(b.t.start=Math.max(f,d)));var e=b.t,l=e.start;d={wsrt:b.wsrt};for(var n=0,h;h=u[n++];){var p=e[h];p&&l&&(d[h]=p-l)}0<f&&(d.gsasrt=b.t.start-f);f=b.e;b="/gen_204?s="+google.sn+"&t=aft&atyp=csi&ei="+google.kEI+"&rt=";e="";for(g in d)b+=""+e+g+
"."+d[g],e=",";for(var G in f)b+="&"+G+"="+f[G];window._cshid&&(b+="&cshid="+window._cshid);2==k()&&(b+="&bb=1");1==k()&&(b+="&r=1");if("gsasrt"in d){var g=v("qsd");0<g&&(b+="&qsd="+g)}google.kBL&&(b+="&bl="+google.kBL);g=b;navigator.sendBeacon?navigator.sendBeacon(g,""):google.log("","",g)}}if(null!==google.aftq&&(g=2==google.ftick||3==google.ftick?google.ftick:1,2==g&&c||1==g&&a||3==g&&(a||c))){var H;for(a=0;c=null==(H=google.aftq)?void 0:H[a++];)try{c()}catch(N){google.ml(N,!1)}google.aftq=null}}}
var O="src bsrc url ll image img-url".split(" ");function P(a){for(var c=0,b;b=O[c++];)if(a.getAttribute("data-"+b))return!0;return!1}google.c.b("il");google.c.setup=function(a,c,b){var d=a.getAttribute("data-atf");if(d)return Number(d);var f="string"!=typeof a.src||!a.src,e=!!a.getAttribute("data-bsrc");d=a.getAttribute("data-deferred");var l=!d&&P(a);l&&a.setAttribute("data-lzy_",1);var n=m(a,e&&google.c.lmv);a.setAttribute("data-atf",n);var h=!!(n&1);f=(f||a.complete)&&!d&&!e&&!(google.c.ll&&h&&l);e=!google.c.lhc&&Number(a.getAttribute("data-iml"))||0;++x;if(f&&!e||a.hasAttribute("data-noaft"))++y;else{if(l=google.c.btfi&&n&4&&e&&I<w){var p=
a.getBoundingClientRect().top+window.pageYOffset;!b||p<b?I=h?w:p:l=!1}h&&(++B,d&&++D);c&&++z;l&&J("aft",e,!1,!0);f&&e?K(c,h,google.c.btfi?0:e):(h&&(!b||b>=w)&&(I=w),google.rll(a,!0,function(){K(c,h,Date.now())}))}return n};google.c.ubr=function(a,c,b){google.c.btfi?0>I&&(b&&(I=b),J("aft",c)):J("aft",c,!0);E&&(E=!1,L());a&&F&&(J("prt",c),J("iml",c,!0),F=!1,M(),google.c.setup=function(){return 0},google.c.ubr=function(){})};}).call(this);(function(){
var b=[function(){google.tick&&google.tick("load","dcl")}];google.dclc=function(a){b.length?b.push(a):a()};function c(){for(var a;a=b.shift();)a()}window.addEventListener?(document.addEventListener("DOMContentLoaded",c,!1),window.addEventListener("load",c,!1)):window.attachEvent&&window.attachEvent("onload",c);}).call(this);(function(){
var b=[];google.jsc={xx:b,x:function(a){b.push(a)},mm:[],m:function(a){google.jsc.mm.length||(google.jsc.mm=a)}};}).call(this);(function(){
var e=this||self;

var g={};function w(a,b){if(null===b)return!1;if("contains"in a&&1==b.nodeType)return a.contains(b);if("compareDocumentPosition"in a)return a==b||!!(a.compareDocumentPosition(b)&16);for(;b&&a!=b;)b=b.parentNode;return b==a};var y=function(a,b){return function(d){d||(d=window.event);return b.call(a,d)}},D="undefined"!=typeof navigator&&/Macintosh/.test(navigator.userAgent),E=function(){this._mouseEventsPrevented=!0};
var F=function(){this.h=this.g=null},H=function(a,b){var d=G;d.g=a;d.h=b;return d};F.prototype.i=function(){var a=this.g;this.g&&this.g!=this.h?this.g=this.g.__owner||this.g.parentNode:this.g=null;return a};var I=function(){this.j=[];this.g=0;this.h=null;this.l=!1};I.prototype.i=function(){if(this.l)return G.i();if(this.g!=this.j.length){var a=this.j[this.g];this.g++;a!=this.h&&a&&a.__owner&&(this.l=!0,H(a.__owner,this.h));return a}return null};var G=new F,J=new I;
var N=function(){this.s=[];this.g=[];this.h=[];this.l={};this.i=null;this.j=[];K(this,"_custom")},O="undefined"!=typeof navigator&&/iPhone|iPad|iPod/.test(navigator.userAgent),P=String.prototype.trim?function(a){return a.trim()}:function(a){return a.replace(/^\s+/,"").replace(/\s+$/,"")},Q=/\s*;\s*/,da=function(a,b){return function l(c,f){f=void 0===f?!0:f;var k=b;if("_custom"==k){k=c.detail;if(!k||!k._type)return;k=k._type}var m=k;"click"==m&&(D&&c.metaKey||!D&&c.ctrlKey||2==c.which||null==c.which&&
4==c.button||c.shiftKey)?m="clickmod":"keydown"==m&&!c.a11ysc&&(m="maybe_click");var u=c.srcElement||c.target;k=R(m,c,u,"",null);if(c.path){J.j=c.path;J.g=0;J.h=this;J.l=!1;var L=J}else L=H(u,this);for(var p;p=L.i();){var h=p;var q=void 0;var r=h;p=m;var n=r.__jsaction;if(!n){var x;n=null;"getAttribute"in r&&(n=r.getAttribute("jsaction"));if(x=n){n=g[x];if(!n){n={};for(var z=x.split(Q),aa=z?z.length:0,A=0;A<aa;A++){var v=z[A];if(v){var B=v.indexOf(":"),M=-1!=B,ba=M?P(v.substr(0,B)):"click";v=M?P(v.substr(B+
1)):v;n[ba]=v}}g[x]=n}r.__jsaction=n}else n=ca,r.__jsaction=n}r=n;"maybe_click"==p&&r.click?(q=p,p="click"):"clickkey"==p?p="click":"click"!=p||r.click||(p="clickonly");q={o:q?q:p,action:r[p]||"",event:null,u:!1};k=R(q.o,q.event||c,u,q.action||"",h,k.timeStamp);if(q.u||q.action)break}k&&"touchend"==k.eventType&&(k.event._preventMouseEvents=E);if(q&&q.action){if("mouseenter"==m||"mouseleave"==m)if(u=c.relatedTarget,!("mouseover"==c.type&&"mouseenter"==m||"mouseout"==c.type&&"mouseleave"==m)||u&&(u===
h||w(h,u)))k.action="",k.actionElement=null;else{m={};for(var t in c)"function"!==typeof c[t]&&"srcElement"!==t&&"target"!==t&&(m[t]=c[t]);m.type="mouseover"==c.type?"mouseenter":"mouseleave";m.target=m.srcElement=h;m.bubbles=!1;k.event=m;k.targetElement=h}}else k.action="",k.actionElement=null;h=k;a.i&&!h.event.a11ysgd&&(t=R(h.eventType,h.event,h.targetElement,h.action,h.actionElement,h.timeStamp),"clickonly"==t.eventType&&(t.eventType="click"),a.i(t,!0));if(h.actionElement||"maybe_click"==h.eventType)if(a.i)!h.actionElement||
"A"!=h.actionElement.tagName||"click"!=h.eventType&&"clickmod"!=h.eventType||(c.preventDefault?c.preventDefault():c.returnValue=!1),(c=a.i(h))&&f&&l.call(this,c,!1);else{if((f=e.document)&&!f.createEvent&&f.createEventObject)try{var C=f.createEventObject(c)}catch(ha){C=c}else C=c;h.event=C;a.j.push(h)}}},R=function(a,b,d,c,f,l){return{eventType:a,event:b,targetElement:d,action:c,actionElement:f,timeStamp:l||Date.now()}},ca={},ea=function(a,b){return function(d){var c=a,f=b,l=!1;"mouseenter"==c?c=
"mouseover":"mouseleave"==c&&(c="mouseout");if(d.addEventListener){if("focus"==c||"blur"==c||"error"==c||"load"==c)l=!0;d.addEventListener(c,f,l)}else d.attachEvent&&("focus"==c?c="focusin":"blur"==c&&(c="focusout"),f=y(d,f),d.attachEvent("on"+c,f));return{o:c,m:f,capture:l}}},K=function(a,b){if(!a.l.hasOwnProperty(b)){var d=da(a,b),c=ea(b,d);a.l[b]=d;a.s.push(c);for(d=0;d<a.g.length;++d){var f=a.g[d];f.h.push(c.call(null,f.g))}"click"==b&&K(a,"keydown")}};N.prototype.m=function(a){return this.l[a]};var V=function(a,b){var d=new fa(b);a:{for(var c=0;c<a.g.length;c++)if(S(a.g[c],b)){b=!0;break a}b=!1}if(b)return a.h.push(d),d;T(a,d);a.g.push(d);U(a);return d},U=function(a){for(var b=a.h.concat(a.g),d=[],c=[],f=0;f<a.g.length;++f){var l=a.g[f];W(l,b)?(d.push(l),X(l)):c.push(l)}for(f=0;f<a.h.length;++f)l=a.h[f],W(l,b)?d.push(l):(c.push(l),T(a,l));a.g=c;a.h=d},T=function(a,b){var d=b.g;O&&(d.style.cursor="pointer");for(d=0;d<a.s.length;++d)b.h.push(a.s[d].call(null,b.g))},Y=function(a,b){a.i=b;a.j&&
(0<a.j.length&&b(a.j),a.j=null)},fa=function(a){this.g=a;this.h=[]},S=function(a,b){for(a=a.g;a!=b&&b.parentNode;)b=b.parentNode;return a==b},W=function(a,b){for(var d=0;d<b.length;++d)if(b[d].g!=a.g&&S(b[d],a.g))return!0;return!1},X=function(a){for(var b=0;b<a.h.length;++b){var d=a.g,c=a.h[b];d.removeEventListener?d.removeEventListener(c.o,c.m,c.capture):d.detachEvent&&d.detachEvent("on"+c.o,c.m)}a.h=[]};var Z=new N;V(Z,window.document.documentElement);K(Z,"click");K(Z,"focus");K(Z,"focusin");K(Z,"blur");K(Z,"focusout");K(Z,"error");K(Z,"load");K(Z,"change");K(Z,"dblclick");K(Z,"input");K(Z,"keyup");K(Z,"keydown");K(Z,"keypress");K(Z,"mousedown");K(Z,"mouseenter");K(Z,"mouseleave");K(Z,"mouseout");K(Z,"mouseover");K(Z,"mouseup");K(Z,"paste");K(Z,"touchstart");K(Z,"touchend");K(Z,"touchcancel");K(Z,"speech");(function(a){google.jsad=function(b){Y(a,b)};google.jsaac=function(b){return V(a,b)};google.jsarc=function(b){X(b);for(var d=!1,c=0;c<a.g.length;++c)if(a.g[c]===b){a.g.splice(c,1);d=!0;break}if(!d)for(d=0;d<a.h.length;++d)if(a.h[d]===b){a.h.splice(d,1);break}U(a)}})(Z);window.gws_wizbind=function(a){return{trigger:function(b){var d=a.m(b.type);d||(K(a,b.type),d=a.m(b.type));var c=b.target||b.srcElement;d&&d.call(c.ownerDocument.documentElement,b)},bind:function(b){Y(a,b)}}}(Z);}).call(this);</script> <script nonce="k5Jw/eNXCbD5/lgt7TFi5g==">(function(){google.xjs={ck:'xjs.s.mX-1p2fNvUU.L.W.O',cs:'ACT90oHGA6xvtyIN2gVmSRh1fbg59zs8XQ',excm:[]};})();</script>   <script nonce="k5Jw/eNXCbD5/lgt7TFi5g==">(function(){window.google.xjsu='/xjs/_/js/k\x3dxjs.s.en_US.bh4POd2q-ow.O/m\x3dcdos,dpf,hsm,jsa,d,csi/am\x3dwEAEAAAAECBQgBQAAAAAAKAACIOBAIDmGQAAEYyAgqREAgAAgAnsAwL-mwDABZsYAAAAAAAQgEugUWogURCAAAAAAFldnQARAAE/d\x3d1/dg\x3d2/br\x3d1/rs\x3dACT90oH7nqgVbjFOjDzNXn8NxEt9g_wkIQ';})();function _DumpException(e){throw e;}
function _F_installCss(c){}
</script>  <script defer="" src="/xjs/_/js/k=xjs.s.en_US.bh4POd2q-ow.O/m=cdos,dpf,hsm,jsa,d,csi/am=wEAEAAAAECBQgBQAAAAAAKAACIOBAIDmGQAAEYyAgqREAgAAgAnsAwL-mwDABZsYAAAAAAAQgEugUWogURCAAAAAAFldnQARAAE/d=1/dg=2/br=1/rs=ACT90oH7nqgVbjFOjDzNXn8NxEt9g_wkIQ" nonce="k5Jw/eNXCbD5/lgt7TFi5g=="></script>    <script nonce="k5Jw/eNXCbD5/lgt7TFi5g==">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.8dERVtYpEbk.O","com","en","538",0,[4,2,".40.40.40.40.40.40.","","1300102,3700258,3700817,3700831,3700874","367915296","0"],null,"AwN6YPO0AY-t0PEPtN-SyAc",null,0,"og.qtm.DcFyqEcRUTY.L.W.O","AA2YrTtK8xRmj0fyGPTOEIIC57ejY0deLQ","AA2YrTtSjyfGhHQrwA20fAkBWvJK9pi4mQ","",2,1,200,"USA",null,null,"1","538",1],null,[1,0.1000000014901161,2,1],[1,0.001000000047497451,1],[1,0,0,null,"0","lymanmcbride@gmail.com","","AOEwXKpmrYQ4GOTroWgo-cSfpos7hGxVs_zRCKKq7QhGwO2at0ZYzsAXtRWhYI3A7ZPIo_MDZpOrA-GP64rkONybvu-z-q5T8A"],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,1,null,null,0,0,0],["%1$s (default)","Brand account",0,"%1$s (delegated)",1,null,83,"https://www.google.com/webhp?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=538\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=157",0,"dashboard",null,null,null,null,"Profile","",0,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAmgQ","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,0,0,"",null,null,"Session expired",null,null,"https://docs.google.com/picker","Visitor",null,"Default","Delegated","Sign out of all accounts",1,0,null,0,0,0,"myaccount.google.com"],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.jcYff4gdSOQ.O/d=1/ct=zgms/rs=AHpOoo_CvAHQybwQAZJQL2tdeysMj0HgHw/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20210405.0_p0","en",null,0],[0.009999999776482582,"com","538",[["19022520","19022519","7",1,5,2592000,"AN2NJM4gQIuxfIK5hZjNKsc0-TisBGOCvQ:1618608899028","",0,1,2,"https://www.google.com/_/og/promos/",0],"n","",["","",""],1,5184000,null,null,"https://www.google.com/url?q=https://myaccount.google.com%3Futm_medium%3Dhpp%26utm_source%3Dgoogle%26utm_campaign%3Dalp_ga_callout_2\u0026source=hpp\u0026id=19022520\u0026ct=7\u0026usg=AFQjCNGp19HFUQSLNjuW4r1gk8BmlccEDQ",null,null,null,null,null,1,null,0,0,1,0,0,0,null,null,0,0,null,0],null,null,null,0,null,null,["5061451","google\\.(com|ru|ca|by|kz|com\\.mx|com\\.tr)$",1]],[1,1,null,40400,538,"USA","en","367915296.0",8,0.009999999776482582,1,0,null,null,1,0,"3700817,3700831,3700874",null,null,null,"AwN6YPO0AY-t0PEPtN-SyAc",1,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.8dERVtYpEbk.O/rt=j/m=qabr,qgl,q_d,qdid,qcwid,qmutsd,qbg,qbd,qapid,qald/exm=qaaw,qadd,qaid,qein,qhaw,qhbr,qhch,qhga,qhid,qhin,qhpr/d=1/ed=1/rs=AA2YrTtK8xRmj0fyGPTOEIIC57ejY0deLQ"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.DcFyqEcRUTY.L.W.O/m=qdid,qcwid/excm=qaaw,qadd,qaid,qein,qhaw,qhbr,qhch,qhga,qhid,qhin,qhpr/d=1/ed=1/ct=zgms/rs=AA2YrTtSjyfGhHQrwA20fAkBWvJK9pi4mQ"]],null,null,[""],[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?prid=19022520\u0026pgid=19022519\u0026puid=187d6639f8efa830\u0026bc=1"],0,280,420,70,25,0,null,0,null,null,8000,null,71,3,null,[19022520,19022519,"",1,5,"","AN2NJM4gQIuxfIK5hZjNKsc0-TisBGOCvQ:1618608899028",0,5184000,"187d6639f8efa830",0,2,0,"https://www.google.com/url?q=https://myaccount.google.com%3Futm_medium%3Dhpp%26utm_source%3Dgoogle%26utm_campaign%3Dalp_ga_callout_2\u0026source=hpp\u0026id=19022520\u0026ct=7\u0026usg=AFQjCNGp19HFUQSLNjuW4r1gk8BmlccEDQ","https://www.google.com/_/og/promos/",0,0,0],0,null,null,null,0,null,76,null,null,null,107,108,109,""],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/app?bc=1"],0,448,328,57,4,1,0,0,63,64,8000,"https://www.google.com/intl/en/about/products",67,1,69,null,1,70,"Can't seem to load the app launcher right now. Try again or go to the %1$sGoogle Products%2$s page.",3,0,0,74,4000]],1,[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.8dERVtYpEbk.O/rt=j/m=qdsh/d=1/ed=1/rs=AA2YrTtK8xRmj0fyGPTOEIIC57ejY0deLQ"],"1","538",1,0,null,"en",0],[300000,"/u/0","/u/0/_/gog/get","AOEwXKpmrYQ4GOTroWgo-cSfpos7hGxVs_zRCKKq7QhGwO2at0ZYzsAXtRWhYI3A7ZPIo_MDZpOrA-GP64rkONybvu-z-q5T8A","https",0,"aa.google.com","rt=j\u0026sourceid=538","","k5Jw/eNXCbD5/lgt7TFi5g==","",0,0,null,0],[["mousedown","touchstart","touchmove","wheel","keydown"],300000]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0"""

listOFWords(sentence)