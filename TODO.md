# Passman TODO
**Author**: Muneeb Mennad\
**Project Name**: Passman\
**File Name**: TODO.md\
**Project Start**: 2026-01-24\
**Github Profile**: https://github.com/mnbmnd/
___
## Current
- [ ] Add error checking (trys and excepts etc.)

## Hand-off
- [ ] Add "settings" to main menu
- [ ] Add reset password functionality
- [ ] Fix loop in setup menu after too many failed attempts to match
- [ ] Update README.md

## Later
- [ ] Add Settings menu for updating master password
- [ ] Rename prompt to something shorter, maybe psm
- [ ] Implement password vault storage (`passwords.json`)
- [ ] Add fuzzy matching for `passman <site>` CLI
- [ ] Add clipboard support
- [ ] Work on implementing this with vim keys or other keybinds
- [ ] Add TUI (full scale)

## Completed ✓
- [x] Master password authentication with PBKDF2
- [x] Password generation (passphrase + alphanumeric)
- [x] Entropy/strength checker
- [x] Menu system
- [x] Add `has_master_credentials()` function to `authentication.py`
- [x] Update `credentials_menu()` in `main.py`
- [x] Test both scenarios
- [x] Fix functions and file structure
- [x] Fix logging in logic
- [x] Rename password_generator.py to passgen.py
- [x] Rename entropy.py to passcheck.py
- [x] Add the overview section to the splash screen
- [x] Add vscode workspace to ignore
- [x] Fix quitting logic
- [x] Fix bug in login menu logic
- [x] Rewrite the overview section
- [x] Add (improve) menu for passgen and passcheck
- [x] Clean up code (Functions, comments, PEP-8, etc.)

###### END_FILE  
