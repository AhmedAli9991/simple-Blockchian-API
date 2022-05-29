from fastapi import APIRouter, status, HTTPException
from typing import List
from schema import BlockchainSchema 
from db.db import Blockchain
router = APIRouter()
import blockchain as _blockchain
blockchain = _blockchain.Blockchain()

@router.post("/mineBlock",status_code=status.HTTP_200_OK, response_model= BlockchainSchema.block)
async def mine_block(data: str):
    if not blockchain.is_chain_valid():
        raise HTTPException(status_code=400, detail="The blockchain is invalid")
    block = blockchain.mine_block(data=data)

    return block


# endpoint to return the blockchain
@router.get("/blockchain/",status_code=status.HTTP_200_OK, response_model= List[BlockchainSchema.block])
async def get_blockchain():
    if not blockchain.is_chain_valid():
        raise HTTPException(status_code=400, detail="The blockchain is invalid")
    chain = blockchain.chain
    return chain

# endpoint to see if the chain is valid
@router.get("/validate/",status_code=status.HTTP_200_OK, response_model= bool)
def is_blockchain_valid():
    if not blockchain.is_chain_valid():
        raise HTTPException(status_code=400, detail="The blockchain is invalid")

    return blockchain.is_chain_valid()


# endpoint to return the last block
@router.get("/blockchain/last/",status_code=status.HTTP_200_OK, response_model= BlockchainSchema.block)
def previous_block():
    if not blockchain.is_chain_valid():
        raise HTTPException(status_code=400, detail="The blockchain is invalid")
        
    return blockchain.get_previous_block()
