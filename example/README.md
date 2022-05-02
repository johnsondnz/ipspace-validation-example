# pre-commit-hooks
Some out-of-the-box hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit

# Available hooks
- `vlan-duplicates` : Checks for duplicate VLANs in yml files.
- `vlan-keys` : Checks all keys are present for a VLAN.
- `ansible-lint` : [ansible-lint](https://github.com/ansible/ansible-lint)

# Adding Hooks
Clone `pre-commit-example`.  Follow examples.
- python3 hooks go into the `hooks/` dir.
- Add the hook into the `console_scripts` section of setup.cfg
- update `.pre-commit-hooks.yaml`

# Deprecated / replaced hooks
