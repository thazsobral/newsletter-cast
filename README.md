<p align="center">
  <img src="https://images2.imgbox.com/75/13/hTHnCG1d_o.png" width=300 heigth=300 />
</p>

# newsletter-cast

<p align="center">
  <img src="https://th.bing.com/th/id/OIG.8QhfSIM00SYnnIOIIfZf?pid=ImgGn" width=300 heigth=300 />
</p>

Robots that automate the collection, conversion and distribution of newsletters.

```mermaid
flowchart TD;
  email --"raw content"--> collector-bot
  subgraph env
    collector-bot --"treated content"--> common-folder[common folder]
    common-folder --"treated content" --> converter-bot
    converter-bot --"converted content"--> common-folder
    common-folder --"converted content"--> publisher-bot
  end
  publisher-bot --"publication ready"--> distribution-platform[distribution platform]
```

## Workflow
  1. we received your newsletter
  2. collector-bot collects and processes your newsletter information and stores it in a common robots folder
  3. convert-bot converts the processed information (in the bots common folder) and converts it to audio (which is also stored in the bots common folder)
  4. publisher-bot captures the ready audio (in the robots common folder) and publishes it on the platforms available to it
  5. all ready !! your audio file is already distributed !
