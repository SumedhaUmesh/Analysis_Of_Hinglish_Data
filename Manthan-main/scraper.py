from os import error
import requests
import emoji


def scrapeInsta(url):
    captionFile = open('insta_caption.txt', "w", encoding='utf-8')
    commentsFile = open('insta_comments.txt', "w", encoding='utf-8')
    media_links = []

    r = requests.get(url)
    r.raise_for_status()
    if r.status_code != 204:
        try:
            json_data = r.json()
            caption = emoji.get_emoji_regexp().sub("",
                                                   json_data["graphql"]["shortcode_media"]["edge_media_to_caption"][
                                                       "edges"][
                                                       0]['node']['text'])
            # print(caption)
            captionFile.write(caption)
            for _ in range(len(json_data["graphql"]["shortcode_media"]["edge_media_to_parent_comment"]["edges"])):
                comment = emoji.get_emoji_regexp().sub("",
                                                       json_data["graphql"]["shortcode_media"][
                                                           "edge_media_to_parent_comment"][
                                                           "edges"][_]["node"]["text"])
                if comment == '':
                    continue
                # print(comment)
                commentsFile.write(comment)
                commentsFile.write('\n\n')

            try:
                for _ in range(len(json_data["graphql"]["shortcode_media"]["edge_sidecar_to_children"]["edges"])):
                    media_links.append(
                        json_data["graphql"]["shortcode_media"]["edge_sidecar_to_children"]["edges"][_]["node"][
                            "display_url"])

            except KeyError:
                media_links.append(json_data['graphql']['shortcode_media']['display_url'])

            return media_links

        except error as e:
            print(e)

        finally:
            captionFile.close()
            commentsFile.close()
