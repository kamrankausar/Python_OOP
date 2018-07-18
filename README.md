# Python_OOP
If we write a script and that script is not going to use again then their is no use of CLASS.
However, there are a lot of reasons to use OOP.

Some reasons:

    Organization: OOP defines well known and standard ways of describing and defining both data and procedure in code. Both data and procedure can be stored at varying levels of definition (in different classes), and there are standard ways about talking about these definitions. That is, if you use OOP in a standard way, it will help your later self and others understand, edit, and use your code. Also, instead of using a complex, arbitrary data storage mechanism (dicts of dicts or lists or dicts or lists of dicts of sets, or whatever), you can name pieces of data structures and conveniently refer to them.

    State: OOP helps you define and keep track of state. For instance, in a classic example, if you're creating a program that processes students (for instance, a grade program), you can keep all the info you need about them in one spot (name, age, gender, grade level, courses, grades, teachers, peers, diet, special needs, etc.), and this data is persisted as long as the object is alive, and is easily accessible.

    Encapsulation: With encapsulation, procedure and data are stored together. Methods (an OOP term for functions) are defined right alongside the data that they operate on and produce. In a language like Java that allows for access control, or in Python, depending upon how you describe your public API, this means that methods and data can be hidden from the user. What this means is that if you need or want to change code, you can do whatever you want to the implementation of the code, but keep the public APIs the same.

    Inheritance: Inheritance allows you to define data and procedure in one place (in one class), and then override or extend that functionality later. For instance, in Python, I often see people creating subclasses of the dict class in order to add additional functionality. A common change is overriding the method that throws an exception when a key is requested from a dictionary that doesn't exist to give a default value based on an unknown key. This allows you to extend your own code now or later, allow others to extend your code, and allows you to extend other people's code.

    Reusability: All of these reasons and others allow for greater reusability of code. Object oriented code allows you to write solid (tested) code once, and then reuse over and over. If you need to tweak something for your specific use case, you can inherit from an existing class and overwrite the existing behavior. If you need to change something, you can change it all while maintaining the existing public method signatures, and no one is the wiser (hopefully).

