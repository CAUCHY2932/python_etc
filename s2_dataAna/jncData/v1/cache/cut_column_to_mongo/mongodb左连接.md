db.product.aggregate([
     {
       $lookup:
         {
           from: "orders",
           localField: "_id",
           foreignField: "pid",
           as: "inventory_docs"
         }
    },
     { $match : { price : {$gt:20} } },
     { $project: {"inventory_docs":1,"_id":0}}