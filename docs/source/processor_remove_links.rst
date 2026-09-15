.. _processor-remove-links:

Remove Links
============

Introduction
------------

This processor drops whole links from the robot after it has been retrieved from Onshape. It is enabled by default via the ``ProcessorRemoveLinks`` processor and does nothing unless ``remove_links`` is set.

Use it for parts of an assembly that are not part of the robot you want to simulate, such as a controller board, a camera mount or loose hardware that sits in the assembly as its own root node. The ``ignore`` option only strips a part's meshes; a link made only of ignored parts still exports as an empty body, which is what this processor avoids.

``config.json`` entries
-----------------------

.. code-block:: javascript

    {
        // ...
        // General import options (see config.json documentation)
        // ...

        "remove_links": [
            "u2d2_assembly",
            "twin_camera_mount",
            "wing_nut*"
        ]
    }

``remove_links`` *(default: [])*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A list of link names to remove. Names are the exported (slugified) link names, and wildcards ``*`` are allowed. Every joint whose parent or child is a removed link, and every camera attached to one, is removed as well.
