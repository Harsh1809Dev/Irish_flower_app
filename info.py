import streamlit as st
from PIL import Image

def app():
    st.title("INFORMATION PAGE : ")

    st.header("**IRIS-VERSICOLOR**")
    image = Image.open('versicolor.jpg')
    st.image(image,caption="IRIS VERSICOLOR",use_column_width=True)
    st.write("Iris versicolor is also commonly known as the blue flag, harlequin blueflag, larger blue flag, northern blue flag, and poison flag, plus other variations of these names, and in Britain and Ireland as purple iris.")
    st.write('It is a species of Iris native to North America, in the Eastern United States and Eastern Canada. It is common in sedge meadows, marshes, and along streambanks and shores. The specific epithet versicolor means "variously coloured".')
    st.write('It is one of the three Iris species in the Iris flower data set outlined by Ronald Fisher in his 1936 paper "The use of multiple measurements in taxonomic problems" as an example of linear discriminant analysis.')
    st.write("**Description**")
    st.write('Iris versicolor is a flowering herbaceous perennial plant, growing 10–80 cm (4–31 in) high. It tends to form large clumps from thick, creeping rhizomes. The unwinged, erect stems generally have basal leaves that are more than 1 cm (0.5 in) wide. Leaves are folded on the midribs so that they form an overlapping flat fan. The well developed blue flower has 6 petals and sepals spread out nearly flat and have two forms. The longer sepals are hairless and have a greenish-yellow blotch at their base. The inferior ovary is bluntly angled. Flowers are usually light to deep blue (purple and violet are not uncommon) and bloom during May to July. Fruit is a 3-celled, bluntly angled capsule. The large seeds can be observed floating in fall.')
    st.write('**Chemical Constituents**')
    st.write('The species has been implicated in several poisoning cases of humans and animals who consumed the rhizomes, which have been found to contain a glycoside, iridin. The sap can cause dermatitis in susceptible individuals.')
    st.write('**Uses**')
    st.write("The iris has been used as magical plant, with people carrying the root (or rhizome) to get 'financial gain', or it was placed in cash registers to increase busines")
    st.write("**Symbolism**")
    st.write('The iris is the official state flower of the U.S. state of Tennessee. This designation was made in 1933 by the state legislature. Although the law does not specifically define a type of iris, it is generally accepted that the purple iris is the state flower.')
    st.write('The blue flag is the provincial flower of Quebec, having replaced the Madonna lily which is not native to the province.')
    st.write('The Purple Iris is the official flower of Kappa Pi International Honorary Art Fraternity.')

    st.header("**IRIS-SETOSA**")
    image_setosa = Image.open('setosa.jpg')
    st.image(image_setosa,caption="IRIS SETOSA",use_column_width=True)
    st.write('Iris setosa, the bristle-pointed iris, is a species of flowering plant in the genus Iris of the family Iridaceae, it belongs the subgenus Limniris and the series Tripetalae. It is a rhizomatous perennial from a wide range across the Arctic sea, including Alaska, Maine, Canada (including British Columbia, Newfoundland, Quebec and Yukon), Russia (including Siberia), northeastern Asia, China, Korea and southwards to Japan. The plant has tall branching stems, mid green leaves and violet, purple-blue, violet-blue, blue, to lavender flowers. There are also plants with pink and white flowers.')
    st.write('**Description**')
    st.write('Iris setosa is similar in form to a miniature Japanese iris, or a dwarf version of Iris sibirica but a shorter lived version.')
    st.write('The shallowly rooted, large, branching rhizomes spread over time to create large clumps. The rhizomes are grey-brown, thick, and are covered with old (maroon-brown) fibrous leaf remains (of last seasons leaves).')
    st.write('It has branched stems, which are very variable in height, ranging from 10 cm (5 inches) up to 1 m (3 ft) tall. The larger plants can grow beyond the height of the leaves. The roundish stems are between 1.5–9 cm in diameter with 1 to 3 branches.')
    st.write('Iris setosa has mid-green leaves, which are grass-like, and lanceolate (sword-shaped). They have a purplish tinged base and the leaves can measure 30–60 cm (12–24 in) long by 0.8–2.5 cm wide.')
    st.write('The plant has 3–4 flowers per stem (between 6 and 13 for the whole plant, in groups of 3,) and it blooms between June and July.')
    st.write('The large flowers are between 5–8 cm (3–6 in) across, usually 7–8 cm, and come in a range of shades of blue, which can depend on the location. and range from violet, purple-blue, violet-blue, blue, to lavender. Very occasionally, there are pink or white forms.')
    st.write("Like other irises, it has 2 pairs of petals, 3 large sepals (outer petals), known as the 'falls' and 3 inner, smaller petals (or tepals), known as the 'standards'. The sepals can be deeply veined dark purple with a yellow-white signal (centre). The standards are so small, that they are reduced to bristles. Which gives the flower, a flat, three petal appearance.")
    st.write('The perianth tube (floral tube) is about 1 cm long, normally dark blue-violet to red-purple with darker veins.')
    st.write('The plant is self-fertile, being hermaphrodite (have both male and female organs) and it is pollinated by insects. The stamens are about 2 cm long, the anthers are purple and the ovary about 1 cm long.')
    st.write('After the flowers have finished blooming, the seeds ripen between August and September. They are cased within a green seed capsule, which is loculicidal, or cylindrical, (measuring 2.5 cm by 1.25 cm), which turns pale brown when it ripens. It has 6 ribs along its sides.')
    st.write('The pale brown seeds (about 2–3 mm in size) have a distinct raised raphe (tissue ridge) the length of one edge.')
    st.write('**Biochemistry**')
    st.write('In 2012, a genetic study was carried out on Iris laevigata and several of its closely related iris species, including Iris ensata, Iris setosa, Iris halophila, Iris scariosa, Iris potaninii, Iris tenuifolia, Iris bloudowii, and Iris sanguinea. Flavonoids also have been analysed from the flowers and leaves of the Iris japonica (ARISAWA et al., 1973), Iris pseudacorus (WILLIAMS et al., 1986), Iris gracilipes (HAYASHI et al., 1984) and Iris setosa (HAYASHI,1984). As most irises are diploid, having two sets of chromosomes. This can be used to identify hybrids and classification of groupings. It has a chromosome count: 2n=38, found by Simonet in 1934. Specimens from Primorskii Krai in Russia, were found to have a chromosome count of 2n=28. Using chromosome research, a progenitor of Iris setosa has been found to be the parent of Iris versicolor with a progenitor of Iris virginica.')
    st.write('**Taxonomoy**')
    st.write("It has several common names, including 'Beachhead Iris' (because it is tolerant of salt air or maritime conditions, encountered in rocky ground above shorelines, especially known as this in Canada), 'Wild flag iris', 'Alaska iris', 'Arctic Iris' (or Dwarf Arctic Iris, because it grows into the Arctic Circle, and it formerly possessed the taxonomic name 'Iris arctica'), 'Arctic blue flag'. and 'Bristle-pointed iris' (in the UK).")
    st.write("The name 'setosa' is derived from the Latin word 'seta' meaning 'bristle' (or hairy), this refers to the standards being almost absent.")
    st.write('It occasionally gets mixed up with Iris hookeri. Mainly because several synonyms of Iris hookeri, were I. setosa variants (I. setosa var. canadensis Foster, I. setosa f. pallidiflora Fernald, I. setosa subsp. pygmaea C.E.Lundstr. and I. setosa f. zonalis Eames).')
    st.write("It was first published by Link (based on an earlier description by Pallas) in 'Jahrbücher der Gewächskunde' (translated as 'Yearbook of Greenhouse'). (Berlin and Leipzig) in 1820. It was originally described from specimens found in east Siberia. It was then published in William Rickatson Dykes (Iris 1913 p. 92) as 'Iris Brachycuspis', which later regarded as a synonym. In 1824, it was also published as 'Iris brachycuspsi' by Fisch. ex Sims in the Botanical Magazine, which is also now regarded as a synonym.")
    st.write("Iris setosa is an accepted name by the RHS, and gained the Royal Horticultural Society's Award of Garden Merit (RHS AGM).")
    st.write('It is one of the three iris species in the Iris flower data set outlined by Ronald Fisher in his 1936 paper "The use of multiple measurements in taxonomic problems" as an example of linear discriminant analysis.')
    st.write("**Distribution and Habitat**")
    st.write('This is the only iris species that is native to both Asia and North America.')
    st.text('Range')
    st.write('Iris setosa has a circum-arctic distribution ranging from coastal Aleutian islands, Alaska, (including Knik Arm in Anchorage,) and Maine in USA, within Canada (including British Columbia, Newfoundland, Quebec, and the Yukon), within Russia (including near to the lower Lena River, Siberia), northeastern Asia, China (including Manchuria and east Jilin), Korea and southwards to Japan (including Honshu and Hokkaido).')
    st.write("It is thought that the form of I. setosa that grows in Canada is slightly different from the Asian form. In Canada, it is found along the shores of the Gulf of St. Lawrence and as far north as the estuary of Saint-Vallier, in Bellechasse county. It is also found in many Canadian parks including; Glacier Bay National Park, Kobuk Valley National Park, Lake Clark National Park, Wrangell–St. Elias National Park and Preserve, Acadia National Park, Katmai National Park and Kenai Fjords National Park. It is not found north of the Brooks mountain Range in Alaska.")
    st.write("The species is found in large amounts in Akkeshi, in eastern Hokkaido, Japan.")
    st.text('Habitat')
    st.write('Iris setosa is tolerant of many kinds of habitats. It can be found in bogs (or swamps), meadows, beside rivers (or streams), on lake shores, (especially rocky shores), beaches, dunes, headlands and light woodland. It can grow in sand or gravelly soils. Although, normally considered a wetland plant, it does well in dry soil, too. It is normally found at 1,500–2,500 m (4,900–8,200 ft) above sea level.')
    st.write("**Conservation**")
    st.write('It was on the Red List of Japanese endangered plants (listed as critically threatened).')
    st.write('**Cultivation**')
    st.write('Iris setosa is suitable to be grown in the front of a border, miniature versions are also suitable for the rock garden or sinks. It can also be grown in on the sunny edge of a woodland garden. Or in a bog garden (in temperate regions). The iris prefer to grow in moist or wet soils. They can also tolerate bog conditions, especially during the growing season it needs a lot of moisture. It can adapt to various conditions, except heavy clay soils that dry out in summer. They dislike soils containing lime. It prefers to grow in partial shade, as full sun risks drought conditions.')
    st.write('Similar to other rhizomatous irises, the rhizome should be planted with the top of the rhizome uncovered with soil. If covered or planted too deep it risks rotting.')
    st.write('In mild temperate areas, the leaves are evergreen, (surviving the winter). But it is best to tidy up the plant and trim the leaves back before the winter, this reduces wind rockage (and root disturbance), then in spring, new leaves will emerge.')
    st.write('Some authors have suggested that irises are deer-proof. This is thought to be incorrect, the leaves can be eaten but they will grow back.')
    st.write('Aphids Macrosiphum euphorbiae and Myzus ornathus can be found on the plant.')
    st.write('**Hardiness**')
    st.write("Iris setosa is one of the hardiest species of irises, but does needs a cold dormant period in winter, and so does not do as well in warm climates. As a native plant of Alaska, it is extremely cold-hardy (minus thirty degrees F. wouldn't kill it). It would only be killed, if never given any summer at all.")
    st.write("It is hardy to various USDA Zone 3–7, or 3–8  or 4–8 but may tolerate Zone 2 and Zone 9 in perfect conditions.")
    st.write("Propagation")
    st.write('Iris setosa can be propagated by seed or by division.')
    st.write('As with all irises, it can difficult to propagate from seed (in the US). It is easier to do so by rhizome divisions. As, the plant increases naturally by rhizomes. Division is best taken place in spring and autumn if possible, ideally in September (about 4–6 weeks after flowering). It can be annually, but it is better every third year, or whenever the plant has spread so much that the centre of the plant, no longer produces any flowering stems. If the plant, is only divided into thirds or quarters, the new divisions can be planted straight away, but if divided into very small sections (for maximum number of plants), these should be put in a coldframe until the following spring when they should have grown new roots.')
    st.write("It is easier to grow from seed in the UK, because the seed requires a cold period (freeze/thaw period). Seeds of the iris can be shaken from the seed capsule in mid-August. They should be planted into beds or trays in a cold frame. They should be sown into drills 1/4 to 1/2 inch deep. If not sown straight away, they should be frozen (to store them). In spring, the seedlings, should be 'pricked out' into individual pots, when they are large enough to handle. They then can be grown in the greenhouse or cold frame for their first year. Plant out into their permanent positions in late spring or early summer. New plants should be planted in September, It takes at least two years to grow a plant from seed to flowering plant.")
    st.text("Hybrids and cultivars")
    st.write('Iris setosa hybridizes very easily with other Iris species (including Siberian and Californian irises)and is therefore often used by breeders of Iris hybrids.')
    st.write("Many variants are known around the world and there are three known variants in Japan – Iris setosa var. hondoensis, Iris setosa var. nasuensis and Iris 'Shiga Ayame'.")
    st.write("Iris setosa var. hondoensis was found in Hondo, Japan, in 1930. It is approximately 80 cm (31 in) high, robust, low branching, with large purple flowers. It is assumed that it is a hybrid with Iris laevigata. It has a chromosome numbers of 2n=54, but they may be triploids.")
    st.write("Iris setosa var. nasuensis was found near the city of Nasu on Honshu island. It grows up to 1m tall. It has broader leaves then Iris setosa and has large flowers (similar to 'Iris laevigata') but has small bracts. It has a chromosome numbers of 2n=54, but they may be triploids.")
    st.write("Iris 'Shiga Ayame' is a hybrid of Iris setosa and Iris sanguinea. It was found in the Shiga Highlands in near the city of Nagano, in central Honshu in 1930 by Yokouchi and Koidzumi, and it was named after the area in where it was discovered. The inner perianths of this iris are an intermediate type between two parents. These three hybrids of I. setosa are found only in limited areas of Honshu Island.")
    st.write("Iris setosa also form hybrids with larger blue flag. Specimens of such hybrids have been observed on Anticosti Island, Quebec.")
    st.write("**Medicinal and other uses**")
    st.write("Herbalists have used the rhizome of Iris setosa for centuries as an ingredient in various medicines, (similar to the usage of Orris roots). However, all parts of Iris setosa are poisonous. The rhizome contains iridin which is an oleoresin. This substance can affect the liver and digestive organs. It can cause allergic reactions such as severe rashes. It can also cause vomiting or diarrhea. It was used in an ingredient in a poison to put on arrowheads.")
    st.write("Although the plant is poisonous, its starchy roots can be made safe for human consumption via cooking. It is cultivated in Japan for its edible root. The Aleut also made a drink from the roots, to be used as a laxative, but the Iñupiat considered the whole plant poisonous. It is used to make a tincture, when used in small amounts to help soothe lymphatic swelling. It can be combined with arnica as an herbal oil to relieve bruises.")
    st.write("Some Inuit tribes in Alaska also roasted and ground the seeds of the iris to be used as a coffee substitute.")
    st.write("The flower petals can be used to create a violet-blue dye, when it is used with a chrome mordant (or fixing agent).They are also were used as a grass dye for baskets.The rhizomes can also be used to extract a perfume (similar to the essence of violets).")

    st.header("**IRIS-VIRGINICA**")
    image_virginica = Image.open('virginica.jpg')
    st.image(image_virginica,caption="IRIS VIRGINICA",use_column_width=True)
    st.write("Iris virginica, with the common name Virginia iris, is a perennial species of flowering plant, native to eastern North America.")
    st.write("It is common along the coastal plain from Florida to Georgia in the Southeastern United States.")
    st.write('It is one of the three Iris species in the Iris flower data set outlined by Ronald Fisher in his 1936 paper "The use of multiple measurements in taxonomic problems" as an example of linear discriminant analysis.')
    st.write("**Description**")
    st.write("Iris virginica is a perennial plant. The plant has 2 to 4 erect or arching, bright green, lance-shaped leaves that are flattened into one plane at the base. Leaves are 1–3 cm (1⁄2–1 1⁄4 in) wide and are sometimes longer than the flower stalk. The fleshy roots (1–2 cm or 1⁄2–3⁄4 in in diameter) are rhizomes that spread underground. Pale brown, variably shaped seeds are born in three-part fruit capsules (3–6 cm or 1 1⁄4–2 1⁄4 in long, 1–2 cm or 1⁄2–3⁄4 in wide).")
    st.write('The slightly fragrant flowers (4 cm or 1 1⁄2 in long, 7 cm or 2 3⁄4 in across) consist of 3 horizontal sepals, or "falls", and 3 erect petals. The petals and sepals can vary in color from dark-violet to pinkish-white. The sepals have a splash of yellow to yellow-orange at the crest. Each plant has 2 to 6 flowers that bloom from April to May upon a single, erect, 30–90 cm (12–35 in) tall stalk. The stalk is sometimes branched and has a slight zigzag appearance.')
    st.write("**Uses**")
    st.write('The Cherokee use this medicinal plant for traditional medicinal uses. The root is pounded into a paste that is used as a salve for the skin. An infusion made from the root is used to treat ailments of the liver, and a decoction of the root is used to treat "yellowish urine".')
    st.write('It may be one of the Iris species used by the Seminole to treat "shock following alligator-bite".')
