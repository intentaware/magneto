match (campaign:Campaign), (impression:Impression)
  where HAS(campaign.id) AND HAS(impression.campaign) AND campaign.id=impression.campaign
  create (campaign)-[:`Campaign -> Impression`]->(impression)

match (impression:Impression), (meta:ImpressionMeta)
  where HAS(impression.id) AND HAS(meta.impression) AND impression.id=meta.impression
  create(impression)-[:`Impression - > Meta`]->(meta)

match (impression:Impression), (visitor:ImpressionUser), (user:User)
  where HAS(impression.visitor) AND HAS(visitor.id) AND HAS(visitor.user) AND HAS(user.id) AND impression.visitor=visitor.id AND visitor.user=user.id
  create(impression)-[:`Impression - > User`]->(user)
