MATCH (campaign:Campaign), (impression:Impression)
  where HAS(campaign.id) AND HAS(impression.campaign) AND campaign.id=impression.campaign
  create (campaign)-[:`Campaign -> Impression`]->(impression)

match (impression:Impression), (meta:ImpressionMeta)
  where HAS(impression.id) AND HAS(meta.impression) AND impression.id=meta.impression
  create(impression)-[:`Impression - > Meta`]->(meta)

match (impression:Impression), (visitor:ImpressionUser), (user:User)
  where HAS(impression.visitor) AND HAS(visitor.id) AND HAS(visitor.user) AND HAS(user.id) AND impression.visitor=visitor.id AND visitor.user=user.id
  create(impression)-[:`Impression - > User`]->(user)

match (impression:Impression), (visitor:ImpressionUser)
  where HAS(impression.visitor) AND HAS(visitor.id) AND impression.visitor=visitor.id
  create(impression)-[:`Impression - > Visitor`]->(visitor)

match (impression:Impression), (visitor:ImpressionUser), (meta:ImpressionMeta)
  where HAS(impression.visitor) AND HAS(visitor.id) AND HAS(meta.impression) AND impression.visitor=visitor.id AND impression.id=meta.impression
  create(visitor)-[:`Visitor - > Meta`]->(meta)

match (campaign:Campaign), (impression:Impression), (visitor:ImpressionUser)
  where HAS(campaign.id) AND HAS(impression.campaign) AND HAS(impression.visitor) AND HAS(visitor.id) AND campaign.id=impression.campaign AND impression.visitor=visitor.id
  create(campaign)-[:`Campaign -> Visitor`]->(visitor)
