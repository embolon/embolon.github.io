---
layout: post
title:  "JavaScript Notes (1)"
date:   2016-02-03 15:22:54 
categories: programming-notes
tags: 
- javascript
- programming
comments: true
identifier: 000000000109
language: english
---

I will start my JavaScript learning session today, keep notes and document interesting thoughts.

## Basic Knowledges

> JavaScript is a high-level, dynamic, untyped, and interpreted programming language. Alongside HTML and CSS, it is one of the three essential technologies of World Wide Web content production; the majority of websites employ it and it is suppported by all modern Web broswers without plug-ins. JavaScript is prototype-based with first-class include any I/O, such as networking, storage, or graphics facilities, relying for these upon the host environment in which it is embedded.

### Variables

JavaScript uses dynamic typing, that types are associated with values, not with variables. A variable can be assign a string and later change to a integer. But unlike Python, JavaScript still needs to define any new variable. 

{% highlight javascript %}    
var x; // define variable x, which is initialized as "undefined"
var y = null; // define and initiate variable y to "null"
var z = "What is going on?";
{% endhighlight %}

### Object related

JavaScript uses a prototype-based object-oriented programming. It may looks weird, but JavaScript uses prototypes while most others use classes for inheritance. Functions are used as the object constructor, rather than having a special init method or constructor functions. Object method functions are also just like other normal functions, only that method functions has a **this** keyword that is bound to a certain object domain/scope. But we can later bind a normal function with an object and use **this** keyword to refer to the object member.

{% highlight javascript %}
function Person(name, age) {
    this.name = name;
    this.age = age;
    
    this.print = function() {
        console.log(name+" is "+this.age+" years old.");
    }
}

var Jack;
Jack = new Person("Jack", 20);
Jack.print();             // Print "Jack is 20 years old."

function printName() {
    console.log(this.name);
}

var boundPrintName = printName.bind(Jack);
boudnPrintName();         // Print "Jack"
printName.call(Jack);     // Print "Jack"
{% endhighlight %}

### Syntax

Looks very close to the C family, but not that wordy like Java. The hard part for me to learn is the functional properties, which is totally different from previous experience. I will later look into this functional properties. Maybe connect with the Scheme languages to better understand this concept.
