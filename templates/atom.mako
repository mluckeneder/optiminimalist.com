<?xml version="1.0" encoding="utf-8"?>

<feed xmlns="http://www.w3.org/2005/Atom">

        <title>optiminimalist.com</title>
        <link href="http://www.optiminimalist.com/atom.xml" rel="self" />
        <link href="http://www.optiminimalist.com/" />

        <% import time %>
        <updated>${time.strftime('%Y-%m-%dT%H:%M:%S.Z', modtime)}</updated>

        % for id, article in articles:
            <entry>
                    <title>${article['title']}</title>
                    <link href="http://www.optiminimalist.com/${id}" />
                    <updated>${time.strftime('%Y-%m-%dT%H:%M:%S.Z', article['date'])}</updated>
                    <summary>${article['tldr']}</summary>
                    <author>
                          <name>optiminimalist</name>
                          <email>optiminimalist@gmail.com</email>
                    </author>
            </entry>
        % endfor
</feed>
