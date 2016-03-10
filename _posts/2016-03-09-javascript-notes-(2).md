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


    var middle = storage['middle-name'] || "(none)";
    // if storage['middle-name'] is undefined, middle = "(none)"
    var status = flight.status || "unknown";
    // if flight.status is undefined, status = "unknown"


"&&" can be used to look up an undefined value without TypeError


    flight.equipment                           // undefined
    flight.equipment.model                     // throw "TypeError"
    fllght.equipment && flight.equipment.model // undefined


### Reference

object is always refered not copied.


    var a = {}, b = {}, c = {};   // a, b, c are three different empty objects
    var a = b = c = {};           // a, b, c all refers to the same empty object


### Prototype


    if (typeof Object.beget !== 'function') {
        Object.beget = function (o) {
            var F = function () {};
            F.prototype = o;
            return new F();
        };
    }
    var another_stooge = Object.beget(stooge);  // heritage from prototype stooge


### Global Abatement

Only create a single global variable to avoid various issues.


    var MYAPP = {};
    MYAPP.variables = {
        "first-name": "Joe",
        "last-name": "Howard"
    };


Make MYAPP as a variable container.
