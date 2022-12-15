import React from "react";

import SectionComponent from "./components/SectionComponent";
import SectionContent from "./components/SectionContent";
import SectionImage from "./components/SectionImage";
import SectionWrapper from "./components/SectionWrapper";

import ValidatorModal from "./components/ValidatorModal";
import MapModal from "./components/MapModal";
import ContactModal from "./components/ContactModal";

import Page from "../../shared-components/page/Page";

export default function HomeApp() {
  return (
    <Page>
      <ValidatorModal />
      <MapModal />
      <ContactModal />

      <SectionWrapper>
        <SectionComponent>
          <SectionImage src="/assets/images/10514534_608137029303220_1576119164495993877_n.jpg" />
          <SectionContent>
            The Lowdina Orchard was established over 30 years ago by Ian and
            Denise Newnham in the Coal River Valley where the cool climate, rich
            soils and pure water combine to produce the world's best quality
            fruit.
          </SectionContent>
        </SectionComponent>
        <SectionComponent alt>
          <SectionImage src="/assets/images/126177752_3487387864711441_704722324649574732_n.jpg" />
          <SectionContent alt>
            Premium late maturing varieties such as Kordia and Regina are
            sustainably grown with care in their boutique 30ha orchard and
            harvested throughout January and early February.
          </SectionContent>
        </SectionComponent>
        <SectionComponent>
          <SectionImage src="/assets/images/41205977_1789559751160936_4055445619966214144_n.jpg" />
          <SectionContent>
            Cutting edge technology, including vacuum packing, in addition to
            air freighting combine to ensure a quality experience for discerning
            customers around the globe.
          </SectionContent>
        </SectionComponent>
        <SectionComponent alt>
          <SectionImage src="/assets/images/16387059_1149723495144568_109872953157813622_n.jpg" />
          <SectionContent alt>
            Ian, Denise and son Jake welcome you to the exquisite experience of
            Lowdina cherries!
          </SectionContent>
        </SectionComponent>
      </SectionWrapper>
    </Page>
  );
}
