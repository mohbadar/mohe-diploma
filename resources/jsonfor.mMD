# Overview
The JSON Form library is a JavaScript client-side library that takes a structured data model defined using [JSON Schema](http://json-schema.org/) as input and returns a [Bootstrap](http://twitter.github.com/bootstrap/)-friendly HTML form that matches the schema. The layout of the generated HTML form may be entirely fine-tuned through a simple declarative mechanism.

The generated HTML form includes client-side validation logic and provides direct inline feedback to the user upon form submission (provided a JSON Schema validator is available). If values are valid, the JSON Form library uses the submitted values and the data model to create the appropriate JavaScript data object.

This is the reference documentation of the JSON Form Library. If you would rather see the JSON Form Library in action, check the [JSON Form Playground](https://github.com/joshfire/jsonform/tree/master/playground#readme) that lets you try and extend the examples of this doc.

# <a name="toc"></a>Table of Contents
1. [Getting started](#getting-started)
1. [Outline of a JSON Form object](#outline)
1. [Using JSON Schema to describe your data model](#schema)
    1. [Basic JSON Schema example](#schema-basic)
    1. [Hey, that's not pure JSON Schema!](#schema-shortcut)
    1. [Supported types](#schema-supported)
    1. [Building more complex structures](#schema-complex)
    1. [Dealing with arrays](#schema-array)
1. [Default form layout](#default)
    1. [From schema element to form field](#default-mapping)
    1. [Common schema properties](#default-common)
    1. [Order of the input fields in the form](#default-order)
1. [Controlling the layout of the form](#fields)
    1. [A list of fields](#fields-list)
    1. [Referencing nested schema properties](#fields-nested)
    1. [Common field properties](#fields-common)
        1. [Append a message to a field: the `append` property](#fields-common-append)
        1. [Describe a field: the `description` property](#fields-common-description)
        1. [Style the field container: the `htmlClass` property](#fields-common-htmlclass)
        1. [Style the input field: the `fieldHtmlClass` property](#fields-common-fieldhtmlclass)
        1. [Skip field's title: the `notitle` property](#fields-common-notitle)
        1. [Prepend a message to a field: the `prepend` property](#fields-common-prepend)
        1. [Field's title: the `title` property](#fields-common-title)
        1. [Field's placeholder: the `placeholder` property](#fields-common-placeholder)
        1. [Disable a field: the `disabled` property](#fields-common-disabled)
        1. [Mark a field as read-only: the `readonly` property](#fields-common-readonly)
        1. [Mark a field allow empty value: the `allowEmpty` property](#fields-common-allowEmpty)
    1. [Text input fields](#fields-strings)
        1. [Simple text: the `text` type](#fields-text)
        1. [Gathering secrets: the `password` type](#fields-password)
        1. [Large text: the `textarea` type](#fields-textarea)
        1. [Code (JavaScript, JSON...): the `ace` type](#fields-ace)
        1. [Color picker: the `color` type](#fields-color)
        1. [A number: the `range` type](#fields-range)
        1. [Gathering preformatted strings: other HTML5 input types](#fields-specialtext)
    1. [Checkbox fields](#fields-check)
        1. [Boolean flag: the `checkbox` type](#fields-checkbox)
        1. [Multiple options: the `checkboxes` type](#fields-checkboxes)
    1. [Selection fields](#fields-selection)
        1. [Selection list: the `select` type](#fields-select)
        1. [A list of radio buttons: the `radios` type](#fields-radios)
        1. [Image selector: the `imageselect` type](#fields-imageselect)
    1. [Groups of fields](#fields-groups)
        1. [Set of fields: the `fieldset` type](#fields-fieldset)
        1. [Advanced options section: the `advancedfieldset` type](#fields-advancedfieldset)
        1. [Authentication settings section: the `authfieldset` type](#fields-authfieldset)
        1. [Generic group: the `section` type](#fields-section)
        1. [Group of buttons: the `actions` type](#fields-actions)
    1. [Arrays](#fields-arrays)
        1. [Generic array: the `array` type](#fields-array)
        1. [Arrays with tabs: the `tabarray` type](#fields-tabarray)
    1. [Alternative sections](#fields-alternative)
        1. [Alternative: the `selectfieldset` type](#fields-selectfieldset)
    1. [Buttons](#fields-buttons)
        1. [Submit the form: the `submit` type](#fields-submit)
        1. [Action button: the `button` type](#fields-button)
    1. [Miscellaneous fields](#fields-misc)
        1. [Guide users: the `help` type](#fields-help)
        1. [Hidden form values: the `hidden` type](#fields-hidden)
1. [Form submission](#submission)
    1. [Validation](#submission-validation)
    1. [Error reporting](#submission-error)
    1. [Accessing submitted values](#submission-values)
1. [Label/Values templating](#templating)
    1. [Add array item index with `{{idx}}`](#templating-idx)
    1. [Use a field's value as tab legend with `{{value}}` and `valueInLegend`](#templating-value)
    1. [Reference the value of another field with `{{values.xxx}}`](#templating-values)
    1. [The `tpldata` property](#templating-tpldata)
1. [Extending JSON Form with your own fields](#extending)
    1. [Field's _view_ definition](#extending-view)
    1. [The default template data object](#extending-data)
    1. [Adjusting parameters before the field gets rendered: the `onBeforeRender` function](#extending-onbeforerender)
    1. [Adding event handlers once the field has been created: the `onInsert` function](#extending-oninsert)
    1. [Creating a container field: the `childTemplate` property](#extending-container)
1. [Adding styles to the generated form](#styles)
1. [Using event handlers to react on fields updates in real time](#events)
1. [Using previously submitted values to initialize a form](#previous)
1. [Dependencies](#deps)
1. [License](#license)

# <a name="getting-started"></a>Getting started
To get started with JSON Form, you need to retrieve a copy of the repository, either cloning the git repository or downloading the repository as a [zip file](https://github.com/joshfire/jsonform/zipball/master).

Once you have a local copy on your local hard drive, open the `example.html` file in your favorite Web browser. It contains the following example.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Getting started with JSON Form</title>
    <link rel="stylesheet" style="text/css" href="deps/opt/bootstrap.css" />
  </head>
  <body>
    <h1>Getting started with JSON Form</h1>
    <form></form>
    <div id="res" class="alert"></div>
    <script type="text/javascript" src="deps/jquery.min.js"></script>
    <script type="text/javascript" src="deps/underscore.js"></script>
    <script type="text/javascript" src="deps/opt/jsv.js"></script>
    <script type="text/javascript" src="lib/jsonform.js"></script>
    <script type="text/javascript">
      $('form').jsonForm({
        schema: {
          name: {
            type: 'string',
            title: 'Name',
            required: true
          },
          age: {
            type: 'number',
            title: 'Age'
          }
        },
        onSubmit: function (errors, values) {
          if (errors) {
            $('#res').html('<p>I beg your pardon?</p>');
          }
          else {
            $('#res').html('<p>Hello ' + values.name + '.' +
              (values.age ? '<br/>You are ' + values.age + '.' : '') +
              '</p>');
          }
        }
      });
    </script>
  </body>
</html>
```

This page creates a form that asks for user's name and age. The user's name is a required field, while the age is optional. The form gets rendered with two input fields and a submit button. The `onSubmit` function is called upon form submission. If you hit the `Submit` button without entering values or if the age you entered is not a number, error messages appear next to the input fields.

---
[Back to top](#toc)

# <a name="outline"></a>Outline of a JSON Form object
The `$.jsonForm` function takes a JSON Form object as parameter. The basic outline of a JSON Form object is:
```javascript
{
  "schema": {
    // Object that describes the data model
  },
  "form": [
    // Array that describes the layout of the form
  ],
  "onSubmitValid": function (values) {
    // Callback function called upon form submission when values are valid
  }
}
```

The `schema` property is _required_. It describes the structured data model that must be created when the form is submitted. It is a JSON object that follows the [properties](http://tools.ietf.org/html/draft-zyp-json-schema-04#section-5.2) definition of the **JSON Schema specification**. JSON Schema lets you describe the data structure that you'd like to generate from the form as well as constraints on possible values, such as the maximum number of characters that a string may contain. Check [Using JSON Schema to describe your data model](#schema) below for more info.

The `form` property is an array that describes the list and order of fields that compose the form. This property is _optional_. In its absence, a default form is generated from the schema. The structure of a form is not necessarily flat: an item in the form array may describe a group of fields or an array. See [Controlling the layout of the form](#fields) below.

The `onSubmitValid` callback is _optional_ as well but chances are you will want to do something with the values entered by the user when the form is submitted and that callback is the easiest way around. It receives the object generated from the submitted values and the schema, provided the values are valid. If you need to do something special when submitted values are invalid for some reason, rather use the `onSubmit` callback, called whenever the form is submitted, that receives the list of errors as first parameter. Check [Accessing submitted values](#submission-values) below for an overview of the different possibilities.

---
[Back to top](#toc)

# <a name="schema"></a>Using JSON Schema to describe your data model
[JSON Schema](http://tools.ietf.org/html/draft-zyp-json-schema-04) is a JSON based format for defining the structure of JSON data. The RFC specification describes the possible contents of the `schema` property in the JSON Form object. 

## <a name="schema-basic"></a>Basic JSON Schema example
Here is an example of a simple schema with two string properties: a `name` property and a `gender` property. The `gender` is a string that must match one of "male", "female" or "alien".
```json
{
  "name": {
    "title": "Name",
    "description": "Nickname allowed",
    "type": "string"
  },
  "gender": {
    "title": "Gender",
    "description": "Your gender",
    "type": "string",
    "enum": [
      "male",
      "female",
      "alien"
    ]
  }
}
```

The JSON Form library uses the data schema to validate submitted values. For instance, the following JSON object is valid against the above schema:
```json
{
  "name": "François Daoust",
  "gender": "male"
}
```
... whereas the following object is not both because the name is not a string and because the gender is not one of the allowed values:
```json
{
  "name": 42,
  "gender": "machine"
}
```

More importantly, the JSON Form library uses the data schema to build the corresponding form. See this basic example live in the playground and note the use of a select field for the gender enumeration.

---
[Back to top](#toc)

## <a name="schema-shortcut"></a>Hey, that's not pure JSON Schema!
If you've already played with JSON Schema, something may bug you in the above example: it is not fully compliant with JSON Schema. The example should rather be:
```json
{
  "type": "object",
  "properties": {
    "name": {
      "title": "Name",
      "description": "Nickname allowed",
      "type": "string"
    },
    "gender": {
      "title": "Gender",
      "description": "Your gender",
      "type": "string",
      "enum": [
        "male",
        "female",
        "alien"
      ]
    }
  }
}
```

In other words, the wrapping `object` is missing:
```json
{
  "type": "object",
  "properties": {
    contents
  }
}
```

True. Good catch, thanks for noticing... It just happens that, in basically all cases in JSON Form, the first level is going to be an object, so you may simply omit that level and start with the `contents` part directly. That said, if you prefer to stick to a pure JSON Schema format, you can! In fact, if your `contents` part defines a property named `properties`, you _must_ define the wrapping context, otherwise JSON Form won't know that you're talking about a `properties` property and will rather think that you're talking about an object whose properties are the children of the `properties` property. See the problem? Don't worry if you don't, simply avoid fields named `properties` and you'll be safe no matter what.

---
[Back to top](#toc)

## <a name="schema-supported"></a>Supported types
JSON Form supports all JSON Schema [simple types](http://tools.ietf.org/html/draft-zyp-json-schema-03#section-5.1) that make sense in the context of an HTML form:
* `string` for strings
* `number` for numbers, including floating numbers
* `integer` for integers
* `boolean` for booleans
* `array` for arrays
* `object` for objects.

In particular, `null` is not supported because it does not mean much in an HTML form; `any` and union types are not supported either because it's hard to come up with a practical input field that can create any type of data.

Types are the most straightforward constraint you can put on property values. All properties must have a `type`, otherwise JSON Form will go berserk and attempt to destroy the Earth. You may add more constraints using other [JSON Schema attributes](http://tools.ietf.org/html/draft-zyp-json-schema-03#section-5). We've already seen `required` to enforce the presence of a value and `enum` as a way to define a list of possible values. You may also use `maxLength`, `readOnly`, `minItems`, `maxItems` or `pattern` for instance to add constraints that match your needs.

---
[Back to top](#toc)

## <a name="schema-complex"></a>Building more complex structures
The `object` type is interesting because it allows to nest objects and build more complex structures. For instance, you may want to separate properties about an author from the rest of the properties to produce the following data structure:
```json
{
  "message": some text,
  "author": {
    "name": name,
    "gender": gender,
    "magic": magic_number
  }
}
```

The following JSON Schema would do the trick (omitting the wrapping `object` as usual):
```json
{
  "message": {
    "type": "string",
    "title": "Message"
  },
  "author": {
    "type": "object",
    "title": "Author",
    "properties": {
      "name": {
        "type": "string",
        "title": "Name"
      },
      "gender": {
        "type": "string",
        "title": "Gender",
        "enum": [ "male", "female", "alien" ]
      },
      "magic": {
        "type": "integer",
        "title": "Magic number",
        "default": 42
      }
    }
  }
}
```

By default, JSON Form groups all the input fields created from the properties of an `object` together in a `fieldset`:

---
[Back to top](#toc)

## <a name="schema-array"></a>Dealing with arrays
Arrays are a pain to support in a form. By essence, the number of items in an array is up to the user of the form so there needs to be some way to add/remove items. That's just the first step though. You'll quickly want some way to reorder items in an array as well, or to define array items that are more than just a simple input field. Oh, by the way, nesting arrays would be good too, _kthxbai_.

Well, good news, JSON Form does it all for you! Use the `array` type in the schema and... that's it! For instance, let's say you would like the user to input a list of friends, in order to generate an array such as:
```json
[
  { "nick": "tidoust", "gender": "male", "age": 34 },
  { "nick": "titine", "gender": "female", "age": 6 },
  { "nick": "E.T.", "gender": "alien" }
]
```

Here is the schema that you would use:
```json
{
  "schema": {
    "friends": {
      "type": "array",
      "items": {
        "type": "object",
        "title": "Friend",
        "properties": {
          "nick": {
            "type": "string",
            "title": "Nickname",
            "required": true
          },
          "gender": {
            "type": "string",
            "title": "Gender",
            "enum": [ "male", "female", "alien" ]
          },
          "age": {
            "type": "integer",
            "title": "Age"
          }
        }
      }
    }
  }
}
```

You can add/remove items using the corresponding buttons at the end of the array. You can also reorder items using drag-and-drop.

> **NB:** reordering items is only available when the `jQuery.ui.sortable` plug-in is up and running. To set it up, just add the following lines to your HTML page to complete the list of scripts:
> ```html
> <script type="text/javascript" src="deps/opt/jquery.ui.core.js"></script>
> <script type="text/javascript" src="deps/opt/jquery.ui.widget.js"></script>
> <script type="text/javascript" src="deps/opt/jquery.ui.mouse.js"></script>
> <script type="text/javascript" src="deps/opt/jquery.ui.sortable.js"></script>
> ```

There is one important restriction to keep in mind: while JSON Schema allows to define arrays whose items follow different schemas depending on their position in the array, JSON Form only supports arrays whose items are all identical. In other words, the `items` property of an `array` property in the schema definition **must** be an object. For example, while a valid JSON Schema, the following schema is **not allowed** in JSON Form:
```json
{
  "boo": {
    "type": "array",
    "items": [
      { "type": "string" },
      { "type": "number" }
    ]
  }
}
```

---
[Back to top](#toc)

# <a name="default"></a>Default form layout

## <a name="default-mapping"></a>From schema element to form field
To generate the form, the JSON Form library parses the schema recursively and checks the `type` and options of the properties it defines to decide upon the type of HTML form input to append to the form. The following mapping is used:
* A `string` property that defines a list of possible values in an `enum` property generates a **selection field**, i.e. a `<select>` element
* A `string` property that defines a `format` property whose value is `color` generates a **color picker field**
* A generic `string` property generates a **text input** otherwise, i.e. an `<input type="text">` element
* A `number` property generates a **text input**, i.e. an `<input type="number">` element.
* An `integer` property generates a **text input** as well, i.e. an `<input type="text">` element.
* A `boolean` property generates a **checkbox**, i.e. an `<input type="checkbox">` element.
* An `object` property generates a **fieldset**, i.e. a `<fieldset>` element. The fieldset contains the sub-form generated by the object's properties.
* An `array` property generates an **array wrapper** that features _Add/Remove_ buttons and items reordering. Each array item is generated from the sub-form defined in the `items` property of the array (which must be an object and not an array as mentioned in the previous section). The array is initially rendered with one item. That item cannot be removed (note the user may decide to leave that item empty though, meaning the submitted array may well be empty).

---
[Back to top](#toc)

## <a name="default-common"></a>Common schema properties
The JSON Form library uses the information available in the JSON schema to complete each generated field. In particular:
* The `title` property serves as **label** for the input.
* The `description` property is displayed next to the input field **to guide user input**.
* The `default` property sets the **initial value** of a field.
* The `maxLength` property sets the **maxlength** attribute of the input field
* The `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum` properties are used to set corresponding attributes for a range input field.
* The `minItems` and `maxItems` properties are used to restrict the number of items that may be added or removed to an array.
* The `readOnly` property sets the **readonly** attribute of the input field
* The `required` property marks the input field as **required**, adds a `jsonform-required` class to the container markup of the input field for styling purpose and adds a `jsonform-hasrequired` class to the `<form>` tag e.g. to allow one to add a legend that explains that fields marked with an asterisk are required, e.g. with CSS properties such as:

```css
.jsonform-required > label:after {
  content: ' *';
  color: red;
}

.jsonform-hasrequired:after {
  content: '* Required field';
  display: block;
  color: red;
  padding-top: 1em;
}
```

Even when they have no visual effect, schema properties are enforced when the form is submitted.

JSON Form automatically generates an ID for all input fields. IDs are prefixed by `jsonform_` and a form counter to avoid conflicts (and allow JSON Form to be used more than once at the same time in a given page). Check the [JSON Form options](#options) section if you need to override the default prefix for some reason.

JSON Form also sets the `name` attribute of all input fields to the _id_ of the schema property that gave birth to it (the _id_ is basically the path that leads to the property in the schema).

---
[Back to top](#toc)

## <a name="default-order"></a>Order of the input fields in the form
JSON Form follows the order of the JSON Schema's object properties _as they appear to the code_ when it loops over the object using a `for ... in` loop. Now, even though it seems natural to read an object's definition from top to bottom, there is simply no guarantee that an object's properties will come out in any particular order when JSON Form parses the JSON Schema's object. It just happens that, _most of the time_, the order in which the properties appear to the code are the same as the natural top-to-bottom order... but that's only _most of the time_!

In other words, even though it seems to work as you might expect, **you should not assume that the fields of the generated form will follow the order of the properties in the JSON Schema's object**. Is it problematic? It could very well be! Fortunately, JSON Form lets you take control of the layout of the form, let's see how...

---
[Back to top](#toc)

# <a name="fields"></a>Controlling the layout of the form
So far, we've seen how JSON Form turns a JSON schema into an HTML form all on its own. That's great but... the truth is, as soon as you start using JSON Form, you'll come up with new use cases that are not covered by default such as:
* It you ask for a password, you may want to generate a **password** input.
* You may want to add a **_Cancel_ button**, or a snippet of HTML in between two input fields
* You may want to provide your own validation **error messages**.
* You may want to provide **alternative sub-forms** based on some initial choice.
* You may want to hide some input fields in an **_Advanced options_ section**.
* You may want to display a `textarea` for a `string` property, or `radio` buttons for a selection field
* You may want to use a _super dooper_ **image selector** when the field lets the user choose between icons
* You may want to ensure that fields appear in a precise order
* and so on...

In other words, JSON Form's default behavior is all very nice, but it's not quite enough. Power to the people! Great, let's do that... Controlling the layout of the form is precisely the _raison d'être_ of the `form` section in the JSON Form object:
```javascript
{
  "schema": {
    // Data model
  },
  "form": [
    // This is where you can control the layout of the form!
  ]
}
```

Note the split between the data model and the layout. That's on purpose!

## <a name="fields-list"></a>A list of fields
The `form` section describes the list of fields that compose the HTML form. It is a JSON array. Each item in the list describes a section of the resulting form. The order of the sections in the generated HTML form follows the order of the items in the array.

An array item may be:
* A **string with the specific value "\*"**. When JSON Form encounters that value, it generates a form with one field per property defined in the schema, using the [default form layout](#schema-default). Use this specific value for simple forms when you simply want to override the remaining form elements (the _Submit_ button in particular). Keep in mind that the order of the fields in the generated form is likely going to be the one of the properties in the JSON Schema but that this is not guaranteed. Here is an example of a simple form that uses `*`:
```json
[
  "*",
  {
    "type": "submit",
    "title": "Eat this!"
  }
]
```
* A **string that references the name of a property in the schema**. The JSON Form library generates the default field that matches the property. Use this method when you do not need to override the generated field by itself, but simply its position within the resulting form. If you wonder how you may reference properties that are at a nested level (when the schema includes `object` properties), hold on, we'll cover that [in a minute](#fields-nested). An example that would work for the [Basic JSON Schema example](#schema-basic):
```json
[
  "name",
  {
    "type": "help",
    "helpvalue": "The rest of the form is entirely optional, feel free to ignore."
  },
  "gender",
  {
    "type": "submit",
    "title": "Roger"
  }
]
```
* A **JSON object whose `key` property references the name of a property in the schema**. The object may also override some of the properties of the schema property and/or define additional properties to control how JSON Form generates the resulting field. Use this method to change the visual aspect of an input field. For instance, to replace the text input by a textarea in the first example:
```json
[
  {
    "key": "name",
    "type": "textarea"
  },
  "gender",
  {
    "type": "submit",
    "title": "Roger"
  }
]
```
In case you're wondering, using `"gender"` to reference the schema is strictly equivalent to using `{ "key": "gender" }`, only a bit shorter and more convenient to write.
* A **JSON object not linked to any property in the schema**. Use this method to produce additional sections in the form, such as fieldsets, helper text, or expandable sections. We've already seen examples _en passant_ with the `help` and `submit` element types. You could also wrap optional fields in an _Optional_ fieldset:
```json
[
  "name",
  {
    "type": "fieldset",
    "title": "Optional",
    "items": [
      "gender"
    ]
  },
  {
    "type": "submit",
    "title": "Roger"
  }
]
```

When you don't define a `form` section, JSON Form creates a default one for you and generates the corresponding form:
```json
[
  "*",
  {
    "type": "actions",
    "items": [
      {
        "type": "submit",
        "title": "Submit"
      }
    ]
  }
]
```

In other words, it produces a form that contains all properties defined in the schema (represented by the `\*` value) followed by an `actions` fieldset that contains a `submit` button.

---
[Back to top](#toc)

## <a name="fields-nested"></a>Referencing nested schema properties
The examples of the previous section stuck to _flat_ schemas, i.e. schemas that do not contain `object` or `array` properties. Adding these possibilities back in the mix produces nested properties. Property names that appear at a deeper level may not be globally unique across the schema so you cannot simply reference them by name. To reference a property that is listed in the `properties` section of an `object` element, simply use a **dotted notation** to describe the **path that leads to the property** in the schema. For instance, consider the following schema:
```json
{
  "author": {
    "type": "object",
    "properties": {
      "name": {
        "type": "object",
        "properties": {
          "firstname": { "type": "string", "title": "First name" },
          "lastname": { "type": "string", "title": "Last name" }
        }
      }
    }
  }
}
```
To reference the `firstname` property from an element in the `form` section, use `"author.name.firstname"`, as in:
```json
[
  "author.name.firstname",
  "author.name.lastname"
]
```

Similarly, to reference a property that is listed in the `items` section of an `array` element, simply use **square brackets** next to the `array` property name combined with the previous dotted notation. For instance, completing a bit the previous schema to turn it into an array of authors:
```json
{
  "authors": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "name": {
          "type": "object",
          "properties": {
            "firstname": { "type": "string", "title": "First name" },
            "lastname": { "type": "string", "title": "Last name" }
          }
        }
      }
    }
  }
}
```
To reference the `firstname` property from an element in the `form` section, use `"authors[].name.firstname"` as in:
```json
[
  {
    "type": "array",
    "items": {
      "authors[].name.firstname",
      "authors[].name.lastname"
    }
  }
]
```

**Beware:** It is relatively easy to create an _invalid_ form when the schema contains arrays. You can only reference array items from an element in the `form` section that is itself part of an array. Said differently, the _array depth_ of an element in the `form` section must match that of the element it references in the schema. The following `form` section is **not valid** because the form element is not part of an array but still references an array item:
```json
[
  "authors[].name.firstname",
  "authors[].name.lastname"
]
```

---
[Back to top](#toc)

## <a name="fields-common"></a>Common field properties
Most fields (except [groups of fields](#fields-groups)) react to a few common properties that fine-tune the look-and-feel of the field generated by JSON Form. These properties are described below in alphabetic order, and illustrated with this short example:

```json
{
  "schema": {
    "mood": {
      "type": "string",
      "title": "Mood of the day",
      "description": "Describe how you feel with a short adjective",
      "default": "happy"
    }
  },
  "form": [
    {
      "key": "mood",
      "prepend": "I feel",
      "append": "today",
      "notitle": true,
      "htmlClass": "usermood",
      "fieldHtmlClass": "input-small"
    }
  ]
}
```

### <a name="fields-common-append"></a>Append a message to a field: the `append` property
Use this property to insert a suffix after the generated form input. The property accepts an HTML fragment string as value. Note that the suffix is not appended to the final value when the form is submitted. 

See also [`prepend`](#fields-common-prepend)

### <a name="fields-common-description"></a>Describe a field: the `description` property
By default, JSON Form displays the `description` property defined in the schema next to the input field to guide user input. Set this property in the `form` section to override that of the schema element (or to define it if the schema does not).

### <a name="fields-common-htmlclass"></a>Style the field container: the `htmlClass` property
Use this property to define additional classes for the generated field container. Classes must be separated by whitespaces. The term *container* refers to the the `<div>` element that wraps the input field, not to the input field itself. Use the [`fieldHtmlClass`](#fields-common-fieldhtmlclass) property to target the input field.

### <a name="fields-common-fieldhtmlclass"></a>Style the input field: the `fieldHtmlClass` property
Use this property to define additional classes for the generate input field. Classes must be separated by whitespaces. This property is typically useful to set the size of the input field, for instance using regular Bootstrap input sizes:

```json
{
  "key": "longkey",
  "fieldHtmlClass": "input-xxlarge"
}
```

Note the `fieldHtmlClass` property applies to all input fields in the form when it is set in the `params` property of the JSON Form object:

```json
{
  "schema": {},
  "form": [],
  "params": {
    "fieldHtmlClass": "input-small"
  }
}
```

### <a name="fields-common-notitle"></a>Skip field's title: the `notitle` property
Sometimes, you may want JSON Form not to insert a label for the input field. Use this property to ignore the `title` property of the schema element.

### <a name="fields-common-prepend"></a>Prepend a message to a field: the `prepend` property
Use this property to insert a prefix before the generated form input. The property accepts an HTML fragment string as value. Note that the prefix will not appear in the final value when the form is submitted. 

See also [`append`](#fields-common-append)

### <a name="fields-common-title"></a>Field's title: the `title` property
By default, JSON Form uses the `title` property defined in the schema as label for the generated input field. Set this property in the `form` section to override that of the schema element (or to define it if the schema does not).

### <a name="fields-common-placeholder"></a>Field's placeholder: the `placeholder` property
JSON Form sets the `placeholder` attribute of the input field based on the value of this property if available.

### <a name="fields-common-disabled"></a>Disable a field: the `disabled` property
When set, JSON Form sets the `disabled` attribute of the underlying input field. Note the `disabled` state is a purely visual effect: validation does not enforce that the field's value has not changed.

JSON Form also adds a `jsonform-disabled` class on the container `<div>` of the generated field to ease styling, if needed.

### <a name="fields-common-readonly"></a>Mark a field as read-only: the `readonly` property
When set, JSON Form sets the `readonly` attribute of the underlying input field, effectively making the field read-only. The property is also purely visual: validation does not enforce that the field's value has not changed.

JSON Form also adds a `jsonform-readonly` class on the container `<div>` of the generated field to ease styling, if needed.

### <a name="fields-common-allowEmpty"></a>Mark a field allow empty value in the final values: the `allowEmpty` property
When set, JSON Form will include the field with the empty string value in the final values, else the fields with empty value will not be included in the final values object.

---
[Back to top](#toc)

Now that you know how to author the `form` section, reference properties in the underlying schema and fine-tune a few common properties, let's see how we can go a step further and actually change the `type` of field that gets generates. JSON Form includes about 25 different fields, ranging from the usual text input field to tabs and wysiwyg HTML editors. That list will grow over time ; if you cannot find the field you're looking for in the list below, no big deal, check the [Extending JSON Form](#extending) section and create your own!

## <a name="fields-strings"></a>Text input fields
Text input fields are linked to `string` properties in the schema. They may be used to gather anything from a word to a large HTML snippet.

> Check [Selection fields](#fields-selection) if the `string` property defines an `enum` property.

### <a name="fields-text"></a>Simple text: the `text` type
JSON Form generates a `text` field by default for all schema properties of type `string` (save enumerations and colors). Not much to say about it, that's just a regular `<input type="text">` input field!

---
[Back to top](#toc)

### <a name="fields-password"></a>Gathering secrets: the `password` type
If you need to gather a password, simply set the type of the form field's type to `password` to have JSON Form generate an `<input type="password">` input field.

```json
{
  "schema": {
    "pwd": {
      "type": "string",
      "title": "Your secret"
    }
  },
  "form": [
    {
      "key": "pwd",
      "type": "password"
    }
  ]
}
```

---
[Back to top](#toc)

### <a name="fields-textarea"></a>Large text: the `textarea` type
The name says it all. Use `textarea` to generate a `<textarea>` field.

```json
{
  "schema": {
    "comment": {
      "type": "string",
      "title": "Your thoughts"
    }
  },
  "form": [
    {
      "key": "comment",
      "type": "textarea"
    }
  ]
}
```

---
[Back to top](#toc)

<!--
### <a name="fields-wysihtml5"></a>HTML authoring input: the `wysihtml5` type
*TODO: explain how to load the library and make it work
-->

### <a name="fields-ace"></a>Code (JavaScript, JSON...): the `ace` type
[Ace](http://ace.ajax.org/) is a standalone code editor written in JavaScript. It supports many languages. Use the `ace` field to generate a field that features an Ace editor. The corresponding Ace files (mode and/or theme) must be available for this to work properly. The [deps/opt/ace](https://github.com/joshfire/jsonform/tree/master/deps/opt/ace) folder contains a minimal set of files from ACE to render a JavaScript or a JSON input field. These files are copied over from the [src-noconflict](https://github.com/ajaxorg/ace-builds/blob/master/src-noconflict) github folder of the Ace project.

>Note: the code of the `ace.js` needs to be encapsulated in `(function(require,define,requirejs) {...})(undefined,undefined,undefined);` before it may be used within JSON Form. Mode and theme files may be used directly within JSON Form.

```json
{
  "schema": {
    "code": {
      "type": "string",
      "title": "Some JSON"
    }
  },
  "form": [
    {
      "key": "code",
      "type": "ace",
      "aceMode": "json",
      "aceTheme": "twilight",
      "width": "100%",
      "height": "200px"
    }
  ]
}
```

The `aceMode` property sets the input mode. The corresponding mode file must be loaded for this to succeed.

The `aceTheme` property sets the theme. The corresponding theme file must be available for download in the same folder as the `ace.js` file. The theme is optional, default theme is `twilight`.

The `width` and `height` properties let you control the dimensions of the input field.

---
[Back to top](#toc)

### <a name="fields-color"></a>Color picker: the `color` type
JSON Form generates a `color` input field by default for all schema properties of type `string` that also have a `format` property set to `color`.

```json
{
  "schema": {
    "maincolor": {
      "type": "string",
      "title": "Main color",
      "format": "color"
    }
  }
}
```

Internally, JSON Form uses the [Spectrum](http://bgrins.github.com/spectrum/) library to create the color picker, so make sure that you include the `spectrum.js` and `spectrum.css` libraries before using this type of field.

---
[Back to top](#toc)

### <a name="fields-range"></a>A number: the `range` type
JSON Form generates a `text` input field by default for all schema properties of type `number` or `integer`. If the schema includes `minimum` and `maximum` constraints, you may want to generate a `range` input field that recent browsers typically render as a slider.

The example below would create a slider from 7 to 77 with increment steps of 5 (default is 1).

```json
{
  "schema": {
    "age": {
      "type": "integer",
      "title": "Your age category (from 7 to 77)",
      "minimum": 7,
      "maximum": 77,
    }
  },
  "form": [
    {
      "key": "age",
      "type": "range",
      "step": 5
    }
  ]
}
```

The `exclusiveMinimum` and `exclusiveMaximum` JSON Schema properties are also supported.

---
[Back to top](#toc)

### <a name="fields-specialtext"></a>Gathering preformatted strings: other HTML5 input types
You may also set the type of the input field generated for a `string` schema property to one of the possible input types introduced in HTML5 to take advantage of better native controls to guide the user input. Using these new types is safe in the sense that browsers that do not support them simply render a text input field.

On top of the other types mentioned above, JSON Form supports the following HTML5 input types: `date`, `datetime`, `datetime-local`, `email`, `month`, `search`, `tel`, `time`, `url`, `week`.

```json
{
  "schema": {
    "birthdate": {
      "type": "string",
      "title": "Birth date"
    }
  },
  "form": [
    {
      "key": "birthdate",
      "type": "date"
    }
  ]
}
```

Note that these input fields are purely visual effects. The usual constraints that may come with these fields are not enforced when the form is submitted. In other words, the user may enter "Hello world" in a `url` field if the browser does not support that input type. To enforce the format of the string, add similar constraints to the schema itself, for instance by adding a `"format": "url"` property to the underlying schema key.

---
[Back to top](#toc)

## <a name="fields-check"></a>Checkbox fields
Checkbox fields are linked to `boolean` properties in the schema. They may also be linked to `array` properties whose items schema defines a list of possible values in an `enum` property.

### <a name="fields-checkbox"></a>Boolean flag: the `checkbox` type
JSON Form generates a `checkbox` field by default for all schema properties of type `boolean`. The default checkbox is kind of dull because it really displays a little checkbox. You'll probably want some way to define an inline message next to the checkbox for the user. Good news, that's precisely the purpose of the `inlinetitle` property.

```json
{
  "schema": {
    "flag": {
      "type": "boolean",
      "title": "Adult"
    }
  },
  "form": [
    {
      "key": "flag",
      "inlinetitle": "Check this box if you are over 18"
    }
  ]
}
```

---
[Back to top](#toc)

### <a name="fields-checkboxes"></a>Multiple options: the `checkboxes` type
If you need the user to select one or more options among a list of choices, the `checkboxes` form field is for your. It applies to an `array` property whose items schema explicitly defines a list of possible values in an `enum` property.

If you want to replace the values that appear in the schema by more user-friendly values, simply define the mapping between the values and the option's label in a `titleMap` as in the following example.

```json
{
  "schema": {
    "menu": {
      "type": "array",
      "title": "Options",
      "items": {
        "type": "string",
        "title": "Option",
        "enum": [
          "starter",
          "maincourse",
          "cheese",
          "dessert"
        ]
      }
    }
  },
  "form": [
    {
      "key": "menu",
      "type": "checkboxes",
      "titleMap": {
        "starter": "Starter would be great",
        "maincourse": "No way I'll skip the main course",
        "cheese": "Cheddar rules!",
        "dessert": "Thumbs up for a dessert"
      }
    }
  ]
}
```

---
[Back to top](#toc)

## <a name="fields-selection"></a>Selection fields
Selection fields are linked to `string` properties in the schema that define an `enum` property with an enumeration of possible values. Such fields allow the selection of one or more options depending on the type of field.

The enumeration defined in the schema sets the list of values that your application will receive once the form is submitted. If you want to replace these values in the form by more user-friendly messages, define the mapping in the `titleMap` property.

```json
{
  "schema": {
    "gender": {
      "type": "string",
      "title": "Gender",
      "enum": [ "male", "female", "alien" ]
    }
  },
  "form": [
    {
      "key": "gender",
      "titleMap": {
        "male": "Dude",
        "female": "Dudette",
        "alien": "I'm from outer space!"
      }
    }
  ]
}
```

### <a name="fields-select"></a>Selection list: the `select` type
JSON Form generates a `select` field by default for all schema properties of type `string` that define an enumeration list. See above for a typical example.

---
[Back to top](#toc)

### <a name="fields-radios"></a>A list of radio buttons: the `radios` type
If you'd rather see the list of options rendered as radio buttons, use the `radios` type.

```json
{
  "schema": {
    "language": {
      "type": "string",
      "title": "Best language",
      "enum": [ "JavaScript", "Python", "PHP", "Java", "C++", "other" ]
    }
  },
  "form": [
    {
      "key": "language",
      "type": "radios"
    }
  ]
}
```

---
[Back to top](#toc)

### <a name="fields-imageselect"></a>Image selector: the `imageselect` type
The image selector lets the user pick up an image in a list. Internally, the image selector produces a string as any other selection field. It converts the string into actual images when the form is rendered. The image selector is mostly intended for icons and small images for the time being.

```json
{
  "schema": {
    "icon": {
      "title": "Choose an icon",
      "type": "string",
      "enum": [
        "address-book",
        "archive",
        "balloon",
        "calendar",
        "camera",
        "cd",
        "disk",
        "heart",
        "home",
        "mail"
      ]
    }
  },
  "form": [
    {
      "key": "icon",
      "type": "imageselect",
      "imageWidth": 64,
      "imageHeight": 64,
      "imageButtonClass": "btn-inverse",
      "imagePrefix": "http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/64/blue-",
      "imageSuffix": "-icon.png",
      "imageSelectorColumns": 4,
      "imageSelectorTitle": "Random choice"
    }
  ]
}
```

From the example, you can tell that there are a number of properties you may want to provide to control the rendering of the image selector:
* `imageWidth` lets you specify the width of the images to render. It is optional and defaults to `32`.
* `imageHeight` lets you specify the height of the images to render. It is optional and defaults to `32`.
* `imageButtonClass` lets you set a class to the button that wraps each image in the image select. For instance, setting the class to `btn-inverse` with Bootstrap would render the image on a dark background. The propery is optional.
* `imagePrefix` and `imageSuffix` are used to create the final URL of images. In turn, this lets you stick to _simple_ strings in the enumeration that defines the possible images. The final image URL is `imagePrefix + (option value) + imageSuffix`. Both properties are optional and default to an empty string.
* `imageSelectorColumns` lets you set the maximum number of images to display per row in the image selector. The property is optional and defaults to `5`. JSON Form balances the number of items per row and the number of items in the last row. It may render fewer items per row as a result.
* `imageSelectorTitle` is the label of the button that gets displayed when no image has been selected yet. It is optional and defaults to the string `Select...`.

---
[Back to top](#toc)


## <a name="fields-groups"></a>Groups of fields
It is often convenient to group a set of fields together in a form to ease readability and thus improve the user experience. JSON Form provides a few types for that purpose.

### <a name="fields-fieldset"></a>Set of fields: the `fieldset` type
JSON Form generates a `fieldset` for all schema properties of type `object`, but you may also want to generate a fieldset without referencing a schema property at all. As you might expect from the name, a `fieldset` field simply produces a `<fieldset>` element in the resulting form.

When set, the `expandable` boolean property tells JSON Form to render the fieldset's title and only expand the fieldset's section when the user clicks on it. This is typically useful for advanced options that users could skip on first read.

If you're using Bootstrap to style the resulting form, please note that it does not include styles for _expandable_ sections at first. You might want to add a few extra stylesheet properties to your CSS to add a visual hint that the section can be expanded/collapsed, for instance:
```css
.expandable > legend:before {
  content: '\25B8';
  padding-right: 5px;
}
.expanded > legend:before {
  content: '\25BE';
}
```

```json
{
  "schema": {
    "comment": {
      "type": "string",
      "title": "Comment"
    },
    "name": {
      "type": "string",
      "title": "Name"
    },
    "age": {
      "type": "number",
      "title": "Age"
    }
  },
  "form": [
    {
      "key": "comment",
      "type": "textarea"
    },
    {
      "type": "fieldset",
      "title": "Author",
      "expandable": true,
      "items": [
        "name",
        "age"
      ]
    }
  ]
}
```

---
[Back to top](#toc)

### <a name="fields-advancedfieldset"></a>Advanced options section: the `advancedfieldset` type
The `advancedfieldset` type is a _shortcut_ type. It is the same thing as an expandable `fieldset` whose title is _Advanced settings_.

```json
{
  "schema": {
    "name": {
      "type": "string",
      "title": "Name"
    },
    "age": {
      "type": "number",
      "title": "Age"
    }
  },
  "form": [
    "name",
    {
      "type": "advancedfieldset",
      "items": [
        "age"
      ]
    }
  ]
}
```

---
[Back to top](#toc)

### <a name="fields-authfieldset"></a>Authentication settings section: the `authfieldset` type
The `authfieldset` type is a _shortcut_ type. It is the same thing as an expandable `fieldset` whose title is _Authentication settings_.

```json
{
  "schema": {
    "name": {
      "type": "string",
      "title": "Name"
    },
    "key": {
      "type": "string",
      "title": "Access key"
    }
  },
  "form": [
    "name",
    {
      "type": "authfieldset",
      "items": [
        "key"
      ]
    }
  ]
}
```

---
[Back to top](#toc)

### <a name="fields-section"></a>Generic group: the `section` type
From time to time, you'll want to group fields without generating a proper `<fieldset>`. This might be for styling purpose, or as a convenient way to define a tab in a [`tabarray`](#fields-tabarray). The generic `section` type generates a group of fields without title wrapped in a `<div>` element.

```json
{
  "schema": {
    "comment": {
      "type": "string",
      "title": "Comment"
    },
    "name": {
      "type": "string",
      "title": "Name"
    },
    "age": {
      "type": "number",
      "title": "Age"
    }
  },
  "form": [
    {
      "key": "comment",
      "type": "textarea"
    },
    {
      "type": "section",
      "title": "Author",
      "items": [
        "name",
        "age"
      ]
    }
  ]
}
```

---
[Back to top](#toc)

### <a name="fields-actions"></a>Group of buttons: the `actions` type
To highlight the section that contains form [buttons](#fields-buttons), use the `actions` type to wrap button fields in a `<div class="form-actions">` container.

```json
{
  "schema": {
    "search": {
      "type": "string",
      "title": "Search"
    }
  },
  "form": [
    "search",
    {
      "type": "actions",
      "items": [
        {
          "type": "submit",
          "title": "Submit"
        },
        {
          "type": "button",
          "title": "Cancel"
        }
      ]
    }
  ]
}
```

---
[Back to top](#toc)

## <a name="fields-arrays"></a>Arrays
Arrays introduce a new level of interaction with the user, because the number of items in an array is not know a priori, meaning that the user may manage array items while filling out the form. Array items may be arbitrarily complex, which means that adding an array item could very well produce a series of 10 additional input fields, including groups of fields and nested arrays.

Array items are not necessarily bound to one and only one schema array element. They may actually reference array items that are different positions in the schema. This is great because the data model that suits your code may not match the way you might want users to _think_ about that data. It comes with a price, though: if you don't pay attention, it is relatively easy to generate invalid `form` sections, all the more so if you want to play with nested arrays. In particular, beware of references to schema elements from the form section.

The rule of thumb is: **the number of `[]` in references to schema elements must match the depth of the `array` in the `form` section.**

That rule is illustrated in the example below:

```json
{
  "schema": {
    "friends": {
      "type": "array",
      "items": {
        "type": "object",
        "title": "Friend",
        "properties": {
          "nick": {
            "type": "string",
            "title": "Nickname"
          },
          "animals": {
            "type": "array",
            "items": {
              "type": "string",
              "title": "Animal name"
            }
          }
        }
      }
    }
  },
  "form": [
    {
      "type": "array",
      "items": {
        "type": "section",
        "items": [
          "friends[].nick",
          {
            "type": "array",
            "items": [
              "friends[].animals[]"
            ]
          }
        ]
      }
    }
  ]
}
```

### <a name="fields-array"></a>Generic array: the `array` type
JSON Form generates an `array` by default for all properties of type `array` in the JSON Schema. For each array item, JSON Form generates the default form that follows the `items` property of the `array` in the JSON Schema.

The above could simply be written as:
```json
{
  "schema": {...},
  "form": [
    "friends"
  ]
}
```

> There is a slight nuance between that definition and the previous one, though. Keep in mind that the order of the fields in the generated form is not guaranteed if you're not explicit about it: the `animals` subarray could potentially appear before `nick` here.

JSON Form creates a first array item in the generated form that cannot be removed. JSON Form then adds the necessary logic to add/remove array items, as well as to reorder items in the array. Reordering items works through drag-and-drop and is only available when the [jQuery UI Sortable](http://jqueryui.com/demos/sortable/) library is loaded.

As mentioned in the [Dealing with arrays](#schema-array) section, while JSON Schema allow to define arrays whose items follow different schemas depending on their position in the array, JSON Form only supports arrays whose items are all identical (for the time being at least). In other words, the `items` property an `array` field in the form definition **must** be an object (or an array with only one item). This is the reason why a container such as a `section` field is required if children need to contain more than one field.
```json
{
  "type": "array",
  "items": {
    "type": "section",
    "items": [
      "friends[].firstname",
      "friends[].lastname"
    ]
  }
}
```

---
[Back to top](#toc)

### <a name="fields-tabarray"></a>Arrays with tabs: the `tabarray` type
Users will quickly get lost with classic arrays when the number of fields per array item increases. When that happens, switching to a `tabarray` helps roll back to a more manageable situation where the list of array items appears as a list of tabs on the left and where only the details of the selected tab are visible on the right.

Switching to a `tabarray` type of diel is as easy as using the value `tabarray` instead of `array` in the `form` section of the JSON Form object.

```json
{
  "schema": {...},
  "form": [
    {
      "type": "tabarray",
      "items": {
        "type": "section",
        "items": [
          "friends[].nick",
          {
            "type": "array",
            "items": {
              "friends[].animals[]"
            }
          }
        ]
      }
    }
  ]
}
```

Visually, the list of tabs on the left is the only thing that the users gets to see at all times. By default, JSON Form labels tabs _Item xx_ (where _xx_ gets replaced by the index of the tab, starting at 1). That's a good start but you'll probably want more control over the label of the tab so that these values make sense for users. This is where [templating](#templating) comes into play. Internally, JSON Form uses the value of the `legend` property of the potential container that wraps the children of the `tabarray` as tab title. Through templating, you can adjust that value to suit your needs. For instance, _Item xx_ would be represented as `Item {{idx}}`.

On top of the tab index, you can use the value of one of the children as legend for the tab using the `{{value}}` template variable. That variable gets replaced by the value of the first field in the children of the array that sets a `valueInLegend` property. This is illustrated in the following example.

```json
{
  "schema": {
    "thoughts": {
      "type": "array",
      "items": {
        "type": "string",
        "title": "Thought",
        "default": "wtf"
      }
    }
  },
  "form": [
    {
      "type": "tabarray",
      "items": [
        {
          "type": "section",
          "legend": "{{idx}}. {{value}}",
          "items": [
            {
              "key": "thoughts[]",
              "valueInLegend": true
            }
          ]
        }
      ]
    }
  ]
}
```

---
[Back to top](#toc)

## <a name="fields-alternative"></a>Alternative sections
A form may contain fields that only make sense when the user has made a certain choice. For instance, you may want to let the user choose between a _search by text_ and a _search by category_, and adjust fields accordingly based on this choice. This is exactly what alternative sections are for.

### <a name="fields-selectfieldset"></a>Alternative: the `selectfieldset` type
When it encounters a `selectfieldset`, JSON Form creates a select field whose options are the `legend` properties of the field's children. It renders the children associated with the selected option.

```json
{
  "schema": {
    "text": {
      "type": "string",
      "title": "Text"
    },
    "category": {
      "type": "string",
      "title": "Category",
      "enum": [
        "Geography",
        "Entertainment",
        "History",
        "Arts",
        "Science",
        "Sports"
      ]
    }
  },
  "form": [
    {
      "type": "selectfieldset",
      "title": "Make a choice",
      "items": [
        {
          "key": "text",
          "legend": "Search by text"
        },
        {
          "key": "category",
          "legend": "Search by category"
        }
      ]
    }
  ]
}
```

If you need to render more than one field per choice, simply wrap the definition of the choice in a `section` fieldset whose items are the fields to render.

The `selectfieldset` type is typically intended to be a visual abstraction not linked to any particular schema key. That said, you may also want to gather the selected option when the form is submitted. No problem, simply associate the `selectfieldset` with the appropriate schema key through the `key` property *et voilà*:

```json
{
  "schema": {
    "choice": {
      "type": "string",
      "title": "Make a choice",
      "enum": [
        "text",
        "category"
      ]
    },
    "text": {
      "type": "string",
      "title": "Text"
    },
    "category": {
      "type": "string",
      "title": "Category",
      "enum": [
        "Geography",
        "Entertainment",
        "History",
        "Arts",
        "Science",
        "Sports"
      ]
    }
  },
  "form": [
    {
      "type": "selectfieldset",
      "title": "Make a choice",
      "key": "choice",
      "titleMap": {
        "text": "Search by text",
        "category": "Search by category"
      },
      "items": [
        "text",
        "category"
      ]
    }
  ]
}
```

---
[Back to top](#toc)

## <a name="fields-buttons"></a>Buttons
No buttons, no submission, so you'd better include at least a `submit` button in the `form` section of the JSON Form object.

### <a name="fields-submit"></a>Submit the form: the `submit` type
The `submit` field produces a button that submits the form when clicked.
```json
{
  "schema": {...},
  "form": [
    "*",
    {
      "type": "submit",
      "title": "OK Go - This Too Shall Pass"
    }    
  ]
}
```

The generated button has the call `btn-primary` which makes the button blue by default if you're using Bootstrap styles.

### <a name="fields-button"></a>Action button: the `button` type
For other buttons, use the `button` type. Note that generic buttons do not trigger any action when clicked unless you set some event handler. See [Using event handlers to react on fields updates in real time](#events) for more info.

---
[Back to top](#toc)

<!--
## <a name="fields-files"></a>File upload
### <a name="fields-file"></a>Upload a file: the `file` type
### <a name="fields-file-transloadit"></a>Upload a file with transloadit: the `file-transloadit` type

-->

## <a name="fields-misc"></a>Miscellaneous fields
JSON Form includes a couple of fields that do not quite fall in any category.

### <a name="fields-help"></a>Guide users: the `help` type
The `help` field lets you write down some message to guide the user in between two fields. The message to display needs to be specified in a `helpvalue` property. HTML tags are interpreted.

```json
{
  "schema": {...},
  "form": [
    "*",
    {
      "type": "help",
      "helpvalue": "<strong>Click on <em>Submit</em></strong> when you're done"
    },
    {
      "type": "submit",
      "title": "Submit"
    }
  ]
}
```

### <a name="fields-hidden"></a>Hidden form values: the `hidden` type
The `hidden` field lets you pass some value to the submitted object without displaying that value to the user.

```json
{
  "schema": {
    "apikey": {
      "type": "string",
      "title": "API key",
      "default": "supercalifragilisticexpialidocious"
    },
    "text": {
      "type": "string",
      "title": "Search string"
    }
  },
  "form": [
    {
      "key": "apikey",
      "type": "hidden"
    },
    "text",
    {
      "type": "submit",
      "title": "Search"
    }
  ]
}
```

---
[Back to top](#toc)

# <a name="submission"></a>Form submission
The form gets submitted when the user clicks the _submit_ button (so don't forget to include one... see [Submit the form: the `submit` type](#fields-submit)). Upon submission, JSON Form:

1. retrieves all fields values
1. creates the result object from submitted values based on the schema
1. runs the validator if it is available to check constraints
1. highlights potential errors in the form next to the problematic fields
1. reports potential errors and/or passes the result object to the caller

Steps 3 and 4 are optional.

## <a name="submission-validation"></a>Validation
Validation of the values entered by the user relies on the [JSON Schema Validator](https://github.com/garycourt/JSV) library which must be loaded if validation is to be enabled.

Validation is enabled by default. To disable validation, set the `validate` property of the JSON Form object to `false`, as in:
```json
{
  "schema": {...},
  "form": [...],
  "validate": false
}
```

The JSON Schema Validator checks all the constraints expressed in the schema (data type, format, maximum length, number of items...) and reports errors accordingly in an array. Each error basically looks like:
```json
{
  "uri": "urn:uuid:1a52a47d-4c69-4d56-94af-4a8afeabaf73#/text",
  "schemaUri": "urn:uuid:50fae450-67b1-499a-89d8-9d5d2c2d3522#/properties/text",
  "attribute": "maxLength",
  "message": "String is greater than the required maximum length",
  "details": 2
}
```

Unless you want to override the default error reporting mechanism, you should not really need to care about the meaning of the above error properties. Refer to the JSON Schema Validator documentation if you need more details.

## <a name="submission-error"></a>Error reporting
JSON Form highlights errors automatically next to problematic fields, with an error message that tells user why the entered values are wrong.

If you want to override the default behavior, append a `displayErrors` function to the JSON Form object. This may be useful to translate error messages (errors reported by the validator are in English) or to clarify cryptic ones.

```javascript
var formObject = {
  "schema": {...},
  "form": [...],
  "displayErrors": function (errors, formElt) {
    for (var i=0; i<errors.length; i++) {
      errors[i].message = "Avast! Ye best be fixin' that field!";
    }
    $(formElt).jsonFormErrors(errors, formObject);
  }
};
```

## <a name="submission-values"></a>Accessing submitted values
JSON Form calls the `onSubmitValid` callback function with the result object generated from the submitted values when the form is submitted and when the validation did not report any error.

```javascript
var formObject = {
  "schema": {...},
  "form": [...],
  "onSubmitValid": function (values) {
    // "values" follows the schema, yeepee!
    console.log(values);
  }
};
```

If you would like to report a global error message to the user when submitted values are incorrect, use the `onSubmit` function that gets called no matter what once the validation is over.

```javascript
var formObject = {
  "schema": {...},
  "form": [...],
  "onSubmit": function (errors, values) {
    if (errors) {
      alert('Check the form for invalid values!');
      return;
    }
    // "values" follows the schema, yeepee!
    console.log(values);
  }
};
```

---
[Back to top](#toc)

# <a name="previous"></a>Using previously submitted values to initialize a form
Gathering user input is great but that's seldom something you'll do once and for all. Whether it is to fix some value, adjust settings or simply because you can, you'll most probably want to let your users get back to a form that they previously submitted to change some values.

To make that possible, there needs to be some way to initialize a form with previously submitted values. Luckily, there's a JSON Form property for that: it's called `value`. Simply set that property to the JSON Form object with the object generated when the form was previously submitted, and JSON Form will initialize the form accordingly.

Taking back the _friends_ example, here is how you could pass on the list of friends that JSON Form might have generated when the form was submitted:
```json
{
  "schema": {
    "friends": {
      // See "Dealing with arrays"
    }
  },
  "value": {
    "friends": [
      { "nick": "tidoust", "gender": "male", "age": 34 },
      { "nick": "titine", "gender": "female", "age": 6 },
      { "nick": "E.T.", "gender": "alien" }
    ]
  }
}
```

---
[Back to top](#toc)

# <a name="templating"></a>Label/Values templating
Templating lets JSON Form expand tags in a template string before rendering using variables that are evaluated at runtime. If you've already read the [tab array](#fields-tabarray) section of this document, you've already encountered two useful template variables: `{{idx}}` and `{{value}}`. JSON Form also features a more generic form that lets you provide the mapping between variables and their values in the `tpldata` property of the JSON Form object.

The templating system follows the [Mustache](http://mustache.github.com/) syntax (although note it only accepts variables). Templating strings can be used in all string properties that will be rendered in the form, namely `title`, `description`, `legend`,`append`, `prepend`, `inlinetitle`, `default`, `helpvalue`, `value` as well as `titleMap` for enumerations.

## <a name="templating-idx"></a>Add array item index with `{{idx}}`
In arrays, `{{idx}}` gets replaced by the index of the array item, starting at 1.
```json
{
  "schema": {
    "thoughts": {
      "type": "array",
      "items": {
        "title": "A thought",
        "type": "string"
      }
    }
  },
  "form": [
    {
      "type": "array",
      "items": [{
        "key": "thoughts[]",
        "title": "Thought number {{idx}}"
      }]
    }
  ]
}
```
First array field gets labeled _Thought number 1_ in the previous example, then _Thought number 2_ and so on.

## <a name="templating-value"></a>Use a field's value as tab legend with `{{value}}` and `valueInLegend`
The [tab array](#fields-tabarray) section already covers the ins and outs of the `{{value}}` property. It is restricted to direct children of `tabarray` fields for the time being. It gets replaced by the value of the first field that sets the `valueInLegend` flag in the descendants of the `tabarray` field (children, great-children, etc.). This is extremely useful to put a meaningful tab legend.
```json
{
  "schema": {
    "thoughts": {
      "type": "array",
      "title": "Thoughts",
      "items": {
        "type": "string",
        "title": "A thought",
        "default": "Grmpf"
      }
    }
  },
  "form": [
    {
      "type": "tabarray",
      "items": [
        {
          "type": "section",
          "legend": "{{idx}}. {{value}}",
          "items": [
            {
              "key": "thoughts[]",
              "title": "Thought {{idx}}",
              "valueInLegend": true
            }
          ]
        }
      ]
    }
  ]
}
```

## <a name="templating-values"></a>Reference the value of another field with `{{values.xxx}}`
The `{{values.xxx}}` can be used in `value` properties to initialize a field to the value of another field. This could be useful when using a set of values to initialize a form. For instance, let's suppose we already know the first and last name of the user, we may want to ask him to enter a more complete form that asks for his full name for display purpose among other things. This full name could be initialized to the concatenation of the user's first name and last name.

```json
{
  "schema": {
    "firstname": {
      "type": "string",
      "title": "First name"
    },
    "lastname": {
      "type": "string",
      "title": "Last name"
    },
    "fullname": {
      "type": "string",
      "title": "Full name"
    }
  },
  "form": [
    "firstname",
    "lastname",
    {
      "key": "fullname",
      "value": "{{values.firstname}} {{values.lastname}}"
    }
  ],
  "value": {
    "firstname": "François",
    "lastname": "Daoust"
  }
}
```

>Note: the part after `values.` is a key reference, and may point to a nested property if needed, e.g. `values.user.lastname`.

>Note: the `{{values.xx}}` variables get replaced when the form is initialized. In particular, they are not re-evaluated when the user modifies the referenced field's value.

## <a name="templating-tpldata"></a>The `tpldata` property
The `tpldata` property of the JSON Form object lets you specify the mapping between variables and values for the templating system. In turn, it makes it possible to have form definitions such as:
```json
{
  "schema": {
    "age": {
      "type": "integer",
      "title": "Age"
    }
  },
  "form": [
    {
      "key": "age",
      "title": "{{user.name}'s age"
    }
  ],
  "tpldata": {
    "user": { "name": "tidoust" }
  }
}
```

JSON Form applies the data in `tpldata` to the values defined in the `schema` and `form` sections before rendering. In the above example, the title of the resulting age field would be _tidoust's age_.

> **When is templating useful?**
> Templating is not _that useful_ when you control the JSON Form object from A to Z. You could typically already do the string replacement yourself, which would have the huge benefit to keep the JSON Form object relatively simple... Just do it if you can!
> Templating is essentially useful when you'd like to use the same JSON Form object (save its "tpldata" property) in different contexts, e.g. for customization purpose or for different locales.

---
[Back to top](#toc)

# <a name="extending"></a>Extending JSON Form with your own fields
No need to run away and start again from scratch if you need some new type of field that is not yet featured in JSON Form. You can extend JSON Form to suit your needs with just a few lines of code!

Fields in JSON Form are defined and exposed in the `JSONForm.fieldTypes` object. To create a new type of field:

1. create the field's _view_
1. extend the `JSONForm.fieldTypes` with a new property whose name is the type you want to create with the field's view as value.
1. go ahead and use the new type in the `form` section of your JSON Form object. That's it, it should work!

Here is a short example that creates an `htmlsnippet` type of field that lets you inject arbitrary HTML in between two fields in a form:
```javascript
JSONForm.fieldTypes['htmlsnippet'] = {
  template: '<%=node.value%>'
};
```

```json
{
  "schema": {...},
  "form": [
    {
      "type": "htmlsnippet",
      "value": "<strong>Aarrr!</strong>"
    }
  ]
}
```

---
[Back to top](#toc)

## <a name="extending-view"></a>Field's view definition
The most difficult part is of course to design the field in itself. Fields views follow the following structure:

```javascript
var view = {
  // The template describes the HTML that the field will generate.
  // It uses Underscore.js templates.
  template: '<div><div id="<%=node.id%>"><%=value%></div></div>',

  // Set the inputfield flag when the field is a real input field
  // that produces a value. Set the array flag when it creates an
  // array of fields. Both flags are mutually exclusive.
  // Do not set any of these flags for containers and other types
  // of fields.
  inputfield: (true || false || undefined),
  array: (true || false || undefined),

  // Most real input fields should set this flag that wraps the
  // generated content into the HTML code needed to report errors
  fieldtemplate: (true || false),

  // Return the root element created by the field
  // (el is the DOM element whose id is node.id,
  // this function is only useful when el is not the root
  // element in the field's template)
  getElement: function (el) {
    // Adjust the following based on your template. In this example
    // there is an additional <div> so we need to go one level up.
    return $(el).parent().get(0);
  },

  // This is where you can complete the data that will be used
  // to run the template string
  onBeforeRender: function (data, node) {},

  // This is where you can enhance the generated HTML by adding
  // event handlers if needed
  onInsert: function (evt, node) {}
};
```

In a few words, a field is defined as an HTML template that follows [Underscore.js template conventions](http://underscorejs.org/#template). The [data object](#extending-data) that gets passed to this template is described below and may be extended in the `onBeforeRender` function. A couple of flags tell JSON Form whether the field will create a _value_, an _array_ or something (e.g. a container or a field that only contains textual information). Event handlers may be bound to the created DOM element once created in the `onInsert` function.

The `template` property is the only required property. It must create a **root** element.
```javascript
var wrong = '<p>First paragraph</p><p>Second paragraph</p>';
var good = '<div><p>First paragraph</p><p>Second paragraph</p></div>';
```

---
[Back to top](#toc)

## <a name="extending-data"></a>The default template data object
By default, JSON Form generates and passes the following data object to create the HTML from the template string. Actual values obviously depend on the element that is being rendered. 

```javascript
var data = {
  // The form element that describes the field in the form section,
  // with all its properties.
  elt: {},

  // The definition of the underlying property in the schema
  // if the field references one (only set for real input fields)
  schema: {},

  // The "node" that describes the resulting field in form that is
  // being generated. Most useful properties are listed here.
  node: {
    id: '',     // The ID of the field
    title: '',  // The field's title
    legend: '', // The field's legend
    name: '',   // The name of the input field (for real input fields)
    value: ''   // The initial value (may be null or undefined)
  },

  // The initial value of the field. Same as node.value except "value"
  // is an empty string when node.value is null or undefined
  value: '',

  // Helper function to escape a string for use as attribute value
  escape: function (val) {}
};
```

If you wonder how to use these values, just check the template definition of existing fields in [the source code of JSON Form](https://github.com/joshfire/jsonform/blob/master/lib/jsonform.js)

---
[Back to top](#toc)

## <a name="extending-onbeforerender"></a>Adjusting parameters before the field gets rendered: the `onBeforeRender` function
The default template data object may not be enough to create an advanced field. Use the `onBeforeRender` function to extend the data object. That function gets called right before the generation of the HTML (provided it exists, that is).

The function receives the default template data object as first parameter and the form node that represents the field internally. Explaining the ins and outs of the `formNode` class is out of scope for this documentation, I'm afraid, but digging up the code a bit should get you started relatively quickly if you need to use the representation of the form that JSON Form maintains internally for some reason.

```javascript
var view = {
  template: '<div id="<%=node.id%>"><%=myvalue%></div>',
  onBeforeRender: function (data, node) {
    // Compute the value of "myvalue" here
    data.myvalue = "Hey, thanks for reading!";
  }
};
```

---
[Back to top](#toc)

## <a name="extending-oninsert"></a>Adding event handlers once the field has been created: the `onInsert` function
JSON Form inserts the generated HTML in the DOM at the right position in the form and calls `onInsert` once done. This lets you enhance the created element, typically by binding event handlers to the newly created elements as needed.

The `onInsert` function receives an event object as first parameter, which is mostly there for historical reasons and should be viewed as deprecated, and the form node that represents the field internally (same object as for `onBeforeRender`). You may use `node.el` to access the root DOM element that the field created.

```
var view = {
  template: '<div id="<%=node.id%>"><a>Talk to me</a></div>',
  onInsert: function (evt, node) {
    $('a', node.el).click(function () {
      alert('Ni!');
    });
  }
};
```

---
[Back to top](#toc)

## <a name="extending-container"></a>Creating a container field: the `childTemplate` property
Container fields have children that generate additional HTML code (each child may potentially generate a complete sub-form on its own through nesting). JSON Form automatically generates the HTML of the children and makes the concatenation available to the container in the `children` property of the template data object.

```javascript
var view: {
  template: '<div><p>I can haz children.</p><%=children%></div>'
};
```

If you need to wrap the HTML a child generates into some HTML code, define a `childTemplate` function. That function will receive the HTML generated by each child.

```javascript
var view: {
  template: '<ul><%=children%></ul>',
  childTemplate: function (inner) {
    return '<li>' + inner + '</li>';
  }
};
```

---
[Back to top](#toc)

# <a name="styles"></a>Adding styles to the generated form
The JSON Form library generates HTML and a bit of JavaScript to enhance the form, but it does not generate any single line of CSS. That's on purpose! The markup produced by JSON Form is straightforward and [Bootstrap](http://twitter.github.com/bootstrap/)-friendly. This means that you may simply include the Bootstrap CSS file to create a visually appealing form.

Relying on the Bootstrap CSS is by no means compulsory. You may extend it with additional properties or use your own stylesheets. If you need to flag certain tags to ease CSS authoring, use the `htmlClass` property (see [Style the field container: the htmlClass property](#wiki-fields-common-htmlclass).

---
[Back to top](#toc)


# <a name="events"></a>Using event handlers to react on fields updates in real time
Throughout the documentation, we've sticked to a purely declarative `form` definition, which more or less justifies the name of the library (**JSON** Form). Events are an exception to the rule. If you'd like to follow how a field gets updated, add an `onClick` or an `onChange` handler to the field's element definition in the JSON Form object and you should receive the events as they get triggered.

This is particularly useful to set behavior to generic buttons.

```javascript
var jsonform = {
  "schema": {
    "text": {
      "type": "string",
      "title": "Text"
    }
  },
  "form": [
    {
      "key": "text",
      "onChange": function (evt) {
        var value = $(evt.target).val();
        if (value) alert(value);
      }
    },
    {
      "type": "button",
      "title": "Click me",
      "onClick": function (evt) {
        evt.preventDefault();
        alert('Thank you!');        
      }
    }
  ]
};
```

---
[Back to top](#toc)

# <a name="deps"></a>Dependencies
At a minimum, the JSON Form library depends on:
- [jQuery](http://jquery.com/) v1.7.1 or above
- The [Underscore.js](http://documentcloud.github.com/underscore/) utility belt, v1.2.3 or above

The JSON Form library may require further libraries, depending on the features you need for the forms you need to render. In particular:
- [ACE](http://ace.ajax.org/) is needed to render rich text input fields. The [deps/opt/ace](https://github.com/joshfire/jsonform/tree/master/deps/opt/ace) folder contains a minimal set of files from ACE to render a JSON input field. Beware that the code of `ace.js` needs to be encapsulated in `(function(require,define,requirejs) {...})(undefined,undefined,undefined);` before it may be used within JSON Form.
- [Bootstrap](http://twitter.github.com/bootstrap/) v3 or above is more or less needed (unless you enjoy ugly forms, that is) if you don't provide your own styles. JSON Form only needs the `bootstrap.css` file.
- The [JSON Schema Validator](https://github.com/garycourt/JSV) is used to detect and report validation errors upon form submission. The [deps/opt](https://github.com/joshfire/jsonform/tree/master/deps/opt) folder contains a "build" of the JSON Schema Validator for use in JSON Form.
- [Bootstrap Dropdowns](http://twitter.github.com/bootstrap/javascript.html#dropdowns) v2.0.3 or above is needed for `imageselect` fields.
- [jQuery UI Sortable](http://jqueryui.com/demos/sortable/) v1.8.20 or above is required for drag-and-drop support within arrays and tabarrays. Note the plugin itself depends on jQuery IU Core, jQuery UI Mouse, and jQuery UI Widget.
- [wysihtml5](http://jhollingworth.github.com/bootstrap-wysihtml5/) is required if the form uses `wysihtml5` textarea fields.
- [Spectrum](http://bgrins.github.com/spectrum/) is required if the form uses `color` fields.

All of these libraries are in the [deps](https://github.com/joshfire/jsonform/tree/master/deps) folder, although you might want to check their respective Web site for more recent versions.

> NB: JSON Form also uses `JSON.parse` and `JSON.stringify` which is normally already natively supported by all modern browsers. You may use a JSON library otherwise.
