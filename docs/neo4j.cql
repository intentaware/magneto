MATCH (campaign:Campaign), (impression:Impression)
  where HAS(campaign.id) AND HAS(impression.campaign) AND campaign.id=impression.campaign
  create (campaign)-[:`has_impressions`]->(impression)

MATCH (campaign:Campaign), (impression:Impression), (meta:ImpressionMeta)
  where HAS(campaign.id) AND HAS(impression.campaign) AND HAS(meta.impression) AND HAS(meta.city) AND campaign.id=impression.campaign AND impression.id = meta.impression
  create (campaign)-[:`gathered_data`]->(meta)

match (impression:Impression) with impression match (meta:ImpressionMeta)
  where HAS(impression.id) AND HAS(meta.impression) AND HAS(meta.city) AND impression.id=meta.impression
  create(impression)-[:`impression_gathered_data`]->(meta)

match (impression:Impression), (visitor:ImpressionUser), (user:User)
  where HAS(impression.visitor) AND HAS(visitor.id) AND HAS(visitor.user) AND HAS(user.id) AND impression.visitor=visitor.id AND visitor.user=user.id
  create(impression)-[:`mapped_users`]->(user)

match (impression:Impression), (visitor:ImpressionUser)
  where HAS(impression.visitor) AND HAS(visitor.id) AND impression.visitor=visitor.id
  create(impression)-[:`unmapped_users`]->(visitor)

match (impression:Impression) with impression match (visitor:ImpressionUser), (meta:ImpressionMeta)
  where HAS(impression.visitor) AND HAS(visitor.id) AND HAS(meta.impression) AND impression.visitor=visitor.id AND impression.id=meta.impression
  create(visitor)-[:`gathered_data`]->(meta)

match (campaign:Campaign), (impression:Impression), (visitor:ImpressionUser)
  where HAS(campaign.id) AND HAS(impression.campaign) AND HAS(impression.visitor) AND HAS(visitor.id) AND campaign.id=impression.campaign AND impression.visitor=visitor.id
  create(campaign)-[:`unmapped_users`]->(visitor)
