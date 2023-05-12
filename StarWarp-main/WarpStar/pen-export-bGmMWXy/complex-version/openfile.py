# Save file to server
with open(file_path, 'wb') as f:
    f.write(response.content)

# Apply mod patch or launch emulator
if is_mod:
    patched_data = apply_ips_patch(rom_data, mod_data)
    # TODO: Handle errors and return patched ROM as download
else:
    # Launch emulator
    # TODO: Handle errors and launch emulator
