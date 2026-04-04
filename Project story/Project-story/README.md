# Project Story

A Python script to replace placeholders in a story with user-provided inputs, creating a personalized version of the story.

## How It Works

1. The script reads a story from `alien.txt`, identifying placeholders in the format `[placeholder]`.
2. It prompts the user to provide replacements for each placeholder.
3. The placeholders are replaced with the user's inputs, and the final story is displayed.

## Usage

1. Create a file named `alien.txt` in the same directory as `story_alien.py`. Add your story with placeholders in `[placeholder]` format.
2. Run the script:

   ```bash
   python story_alien.py
   ```

3. Follow the prompts to provide replacements for the placeholders.
4. View the updated story in the console.

## Example

### Input (`alien.txt`)

```
The [adjective] alien loves to [verb].
```

### Script Execution

```
Enter replacement for [adjective]: friendly
Enter replacement for [verb]: dance
```

### Output

```
The friendly alien loves to dance.
```

## Requirements

- Python 3.x
- A story file named `alien.txt` with placeholders.