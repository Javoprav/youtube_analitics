import pytest


@pytest.fixture()
def test_data():
    return {
  "kind": "youtube#channelListResponse",
  "etag": "8SOBGAWTP6WNDIT9aoovx8H7Gtk",
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#channel",
      "etag": "FpBWEyPdGpIRWEvE-8KC59BoJu0",
      "id": "UCMCgOm8GZkHp8zJ6l7_hIuA",
      "snippet": {
        "title": "вДудь",
        "description": "Здесь задают вопросы",
        "customUrl": "@vdud",
        "publishedAt": "2014-01-03T06:27:22Z",
        "thumbnails": {
          "default": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJV2Av2ouJAjcHnaA8jokTI4uq6DZLnfHJm6T8vw=s88-c-k-c0x00ffffff-no-rj",
            "width": 88,
            "height": 88
          },
          "medium": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJV2Av2ouJAjcHnaA8jokTI4uq6DZLnfHJm6T8vw=s240-c-k-c0x00ffffff-no-rj",
            "width": 240,
            "height": 240
          },
          "high": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJV2Av2ouJAjcHnaA8jokTI4uq6DZLnfHJm6T8vw=s800-c-k-c0x00ffffff-no-rj",
            "width": 800,
            "height": 800
          }
        },
        "localized": {
          "title": "вДудь",
          "description": "Здесь задают вопросы"
        }
      },
      "statistics": {
        "viewCount": "1947591121",
        "subscriberCount": "10300000",
        "hiddenSubscriberCount": false,
        "videoCount": "164"
      }
    }
  ]
}
None