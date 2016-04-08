---
layout: post
title:  "JavaScript Notes (2)"
date:   2016-03-10 01:47:38 
categories: programming-notes
tags: 
- javascript-programming
comments: true
identifier: 000000000110
language: english
---

After some basic knowledge, I will read some books and gather some useful tips for future reference. 

## JavaScripts: The Good Part


### Object

Number, String, Bool, null and undefined are not objects. JavaScript Object are class-free. They look like a python dictionary.

#### Retrieval

"||" can be used to initialize value

{% highlight javascript %}
var middle = storage['middle-name'] || "(none)";
// if storage['middle-name'] is undefined, middle = "(none)"
var status = flight.status || "unknown";
// if flight.status is undefined, status = "unknown"
{% endhighlight %}

"&&" can be used to look up an undefined value without TypeError

{% highlight javascript %}
flight.equipment                           // undefined
flight.equipment.model                     // throw "TypeError"
fllght.equipment && flight.equipment.model // undefined
{% endhighlight %}

#### Reference

object is always refered not copied.

{%highlight javascript %}
var a = {}, b = {}, c = {};   // a, b, c are three different empty objects
var a = b = c = {};           // a, b, c all refers to the same empty object
{% endhighlight %}

#### Prototype

{% highlight javascript %}
if (typeof Object.beget !== 'function') {
    Object.beget = function (o) {
        var F = function () {};
        F.prototype = o;
        return new F();
    };
}
var another_stooge = Object.beget(stooge);  // heritage from prototype stooge
{% endhighlight %}

#### Global Abatement

Only create a single global variable to avoid various issues.

{% highlight javascript %}
var MYAPP = {};
MYAPP.variables = {
    "first-name": "Joe",
    "last-name": "Howard"
};
{% endhighlight %}

Make MYAPP as a variable container.

---

### Functions

#### Invocation Pattern

**The Method**

this binds to the owner object

**The Function**

this binds to global variable instead of the owner object which is a bad design. Do the below to avoid.

{% highlight javascript %}
myObject.double = funcion () {
    var that = this;
    var helper = function () {
        that.value = add(that.value, that.value); // this does not work here
    };
    helper();
};
{% endhighlight %}

**The Constructor**

with a new in front of the constructor, this will bind to the new object.

{% highlight javascript %}
var Quo = function (string) {
    this.status = string
};

var myQuo = new Quo("confused"); // do not forget "new"
{% endhighlight %}

This is actually not a very good way to make a constructor.

**The Apply**

apply will take an owner object as parameter too.

{% highlight javascript %}
var sum = add.apply(null, [3, 4]); // null will be assigned to this
{% endhighlight %}

#### Augmenting Types

Add method to Function.prototype to make this method available to all functions.

{% highlight javascript %}
Function.prototype.method = function (name, func) {
    this.prototype[name] = func;
    return this;
}; // this is not a function defination, so a ';' is needed
// Function.prototype.method = an anonymous function;
// this function add a method to the owner object

Number.method('interger', function () {
    return Math[this < 0 ? 'ceiling' : 'floor'](this);
});

document.writeln((-10 / 3).integer()); // -3
{% endhighlight %}

#### Scope

Unlike C++, variable does not only live inside the scope. Variable will live in the whole function where it is defined.

#### Memoization

A function with cache.

{% highlight javascript %}
var memoizer = function (memo, fundamental) {
    var shell = function (n) {
         var result = memo[n];
         if (typeof result !== 'number') {
             result = fundamental (shell, n);
             memo[n] = result;
         }
         return result;
    };   // shell is the altimate memoizated function
    return shell;
};

var factorial = memoization([0, 1], function (shell, n) {return n*shell(n-1);});
{% endhighlight %}

---

### Other Tips

1. always use '===' or '!==' instead of '==' or '!='
2. always use 'var foo = function foo () ();' instead of 'function foo () {}' in JavaScript, this clearly claims that foo is a variable, any function in JavaScript is a variable.
3. be cautious when use 'for in' to check all properties of an object, since this will also include function properties (functions are variables too)
