# Social Integration

## Instagram Integration

Recipamatic can extract recipes from Instagram posts, primarily handling video content from cooking accounts.

### Key Components

#### InstaLoader

The `InstaLoader` class in `py/src/recipamatic/social/insta/loader.py` provides the core functionality for Instagram integration:

- Handles authentication to Instagram
- Caches login sessions for efficient access
- Downloads post content including images and videos
- Extracts profile information for recipe attribution

#### Post and Profile Structures

The `py/src/recipamatic/social/insta/structures.py` file defines data structures for Instagram content:

- `PostIg`: Represents an Instagram post with:
  - Post metadata (shortcode, caption, hashtags)
  - Media content references (images, videos)
  - Caching of downloaded media
- `ProfileIg`: Represents an Instagram profile with:
  - User information (username, bio, follower count)
  - Profile picture and other metadata
  - Caching of profile data

### Data Flow for Instagram Recipe Extraction

1. User provides Instagram post URLs (shortcodes)
2. System downloads post content using InstaLoader
3. Video content is extracted and saved locally
4. Whisper transcription is applied to extract spoken recipe instructions
5. Text from post captions and video transcriptions is combined
6. RecipeCoreTranscriber processes the text to create structured recipes

### Storage Structure

Instagram data is stored in the filesystem:

- `/data/ig/posts/{shortcode}/` - Contains post data and media
- `/data/ig/profiles/{username}/` - Contains profile information

### Language Processing

Posts are analyzed to detect language using the `py3langid` library, which helps:

- Identify multilingual content
- Ensure appropriate processing for different languages
- Track content language in recipe metadata

## Future Integration Opportunities

The system is designed to allow for additional social media platforms:

- TikTok integration (similar structure to Instagram)
- YouTube for longer recipe videos
- Recipe websites via structured data extraction

## Related Components

- [Audio Transcription](./4-audio-transcription.md) covers the Whisper transcription used to extract recipe instructions from videos
- [Recipe Core](./2-recipe-core.md) documents how extracted text is converted to structured recipe data
