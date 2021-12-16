# mock_da README

Since starting on an actual DA will be bit too much, Microsoft recommends starting understanding DA using their a mock DA.
It's just a way to simulate DA for a md file. No debugging here, but to show stepping through line by line and examining contents of lines etc. This mock DA contains inside the 'debugger' for md file. We need not worry about that for us what's important is that Mock DA talks to VS Code using DAP. 

This project just tries to demo the mock da.

## Instructions
* Create a folder and open it in vscode
* Create a `.md` file in the folder like this one
* install the mock debug extension from VS Code marketplace. You can search for `mock` in the extension view right here within vscode.
* Press F5 and choose `Mock Debug` in the command palette
* 'Debugging' starts and then you can use the buttons, see the call stack etc.
* After this, if you wish to develop this using the instructions on vscode website: https://code.visualstudio.com/api/extension-guides/debugger-extension#development-setup-for-mock-debug, it's very important that you uninstall the mock debug extension that you installed.
